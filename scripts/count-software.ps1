# Forward all options to the shared Python 3.8+ counter.
# Run with: pwsh.exe -NoProfile -NonInteractive -File scripts/count-software.ps1 --check

$ErrorActionPreference = 'Continue'
$counterPath = Join-Path $PSScriptRoot 'count-software.py'
$counterArguments = @($args | ForEach-Object {
    switch -Exact ($_) {
        '-DryRun' { '--dry-run' }
        '-Check' { '--check' }
        '-Details' { '--details' }
        '-Write' { '--write' }
        default { $_ }
    }
})
$pythonCandidates = @(
    @{ Name = 'python.exe'; Prefix = @() }
    @{ Name = 'python3.exe'; Prefix = @() }
)
foreach ($candidate in $pythonCandidates) {
    $pythonCommand = Get-Command $candidate.Name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $pythonCommand -or $pythonCommand.Source -match '\\WindowsApps\\') { continue }
    $probeArguments = @($candidate.Prefix) + @('-c', 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)')
    try {
        & $pythonCommand.Source @probeArguments
        if ($LASTEXITCODE -ne 0) { continue }
        $runArguments = @($candidate.Prefix) + @($counterPath) + $counterArguments
        & $pythonCommand.Source @runArguments
        exit $LASTEXITCODE
    } catch {
        [Console]::Error.WriteLine('Unable to run Python: ' + $_.Exception.Message)
        exit 2
    }
}
[Console]::Error.WriteLine('Python 3.8 or newer is required. Install Python and make it available on PATH.')
exit 2
