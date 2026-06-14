# 统计仓库中各平台收录的软件数量，并自动更新 README_zh.md 和 README_en.md
# 用法: .\scripts\count-software.ps1
#
# 计数规则（按优先级）：
#   1. <!-- software-count: N -->  手动指定（最高优先级）
#   2. 统计 ## <img 标题的数量       多软件文件中带图标的二级标题
#   3. 统计 # <img 标题的数量        单/多软件文件带图标的一级标题
#   4. 兜底 → 1                     无图标标记但视为 1 款
# 排除: README.md, CLAUDE.md, test.md, config.md

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$root = Split-Path -Parent $PSScriptRoot
$EXCLUDED_NAMES = @('README.md', 'CLAUDE.md', 'test.md', 'config.md')
$PLATFORMS = @('Windows', 'Linux', 'MacOS', 'General', 'Android', 'iOS')

function Count-InFile([string]$path) {
    $lines = Get-Content $path -Encoding UTF8 -ErrorAction SilentlyContinue
    if (-not $lines) { return 1 }

    # 1. 手动指定数量（检查前 20 行）
    foreach ($line in ($lines | Select-Object -First 20)) {
        if ($line -match 'software-count:\s*(\d+)') {
            return [int]$Matches[1]
        }
    }

    # 2. 统计带图标的 h2 标题
    $h2 = @($lines | Where-Object { $_ -match '^## <img' }).Count
    if ($h2 -gt 0) { return $h2 }

    # 3. 统计带图标的 h1 标题
    $h1 = @($lines | Where-Object { $_ -match '^# <img' }).Count
    if ($h1 -gt 0) { return $h1 }

    # 4. 兜底
    return 1
}

function Count-Software([string]$dir) {
    if (-not (Test-Path $dir)) { return 0 }
    $total = 0
    Get-ChildItem $dir -Recurse -Filter '*.md' | ForEach-Object {
        if ($EXCLUDED_NAMES -notcontains $_.Name -and $_.FullName -notmatch '\\test\\') {
            $total += Count-InFile $_.FullName
        }
    }
    return $total
}

function Update-Table([string]$readmePath, [string]$header, [string]$newTable) {
    if (-not (Test-Path $readmePath)) {
        Write-Host "警告：$readmePath 不存在，跳过"
        return
    }
    $lines = Get-Content $readmePath -Encoding UTF8
    $result = [System.Collections.Generic.List[string]]::new()
    $i = 0
    $replaced = $false
    while ($i -lt $lines.Count) {
        if (-not $replaced -and $lines[$i] -like "*$header*") {
            $result.Add($newTable)
            $i++
            while ($i -lt $lines.Count -and $lines[$i].StartsWith('|')) { $i++ }
            $replaced = $true
        } else {
            $result.Add($lines[$i])
            $i++
        }
    }
    [System.IO.File]::WriteAllText($readmePath, ($result -join "`n") + "`n", [System.Text.Encoding]::UTF8)
}

function Make-Table([string[]]$headers, [string[]]$sep, $rows) {
    $lines = @(
        '| ' + ($headers -join ' | ') + ' |'
        '| ' + ($sep -join ' | ') + ' |'
    )
    foreach ($row in $rows) {
        $lines += "| $($row.Platform) | $($row.Ess) | $($row.Opt) | **$($row.Total)** |"
    }
    return $lines -join "`n"
}

# 收集各平台数据
$rows = @()
$grandTotal = 0
foreach ($platform in $PLATFORMS) {
    $ess = Count-Software (Join-Path $root "$platform\Essential")
    $opt = Count-Software (Join-Path $root "$platform\Optional")
    $total = $ess + $opt
    $rows += [PSCustomObject]@{ Platform = $platform; Ess = $ess; Opt = $opt; Total = $total }
    $grandTotal += $total
}

# 输出统计表
Write-Host '## 软件收录统计'
Write-Host ''
Write-Host '| 平台 | Essential | Optional | 合计 |'
Write-Host '|------|-----------|----------|------|'
foreach ($row in $rows) {
    Write-Host "| $($row.Platform) | $($row.Ess) | $($row.Opt) | **$($row.Total)** |"
}
Write-Host ''
Write-Host "总计：$grandTotal 款软件"
Write-Host ''

# 更新中英文 README
$zhTable = Make-Table @('平台','Essential','Optional','合计') @('------','-----------','----------','------') $rows
$enTable = Make-Table @('Platform','Essential','Optional','Total') @('----------','-----------','----------','-------') $rows

Update-Table (Join-Path $root 'README_zh.md') '| 平台 | Essential | Optional | 合计 |' $zhTable
Update-Table (Join-Path $root 'README_en.md') '| Platform | Essential | Optional | Total |' $enTable

Write-Host '✓ README_zh.md 和 README_en.md 已更新'
