#!/bin/bash
# 统计仓库中各平台收录的软件数量，并自动更新 README_zh.md 和 README_en.md
# 用法: bash scripts/count-software.sh
#
# 计数规则（按优先级）：
#   1. <!-- software-count: N -->  手动指定（最高优先级）
#   2. 统计 ## <img 标题的数量       多软件文件中带图标的二级标题
#   3. 统计 # <img 标题的数量        单/多软件文件带图标的一级标题
#   4. 兜底 → 1                     无图标标记但视为 1 款
# 排除: README.md, CLAUDE.md, test.md, config.md

cd "$(dirname "$0")/.." || exit 1

count_in_file() {
    local file="$1"
    local first_lines
    first_lines=$(head -20 "$file" 2>/dev/null)

    # 1. 手动指定数量
    if echo "$first_lines" | grep -q 'software-count:'; then
        echo "$first_lines" | grep 'software-count:' | sed 's/.*software-count:\s*\([0-9]*\).*/\1/' | head -1
        return
    fi

    # 2. 统计带图标的 h2/h1 标题数
    local h2_count h1_count
    h2_count=$(grep -c '^## <img' "$file" 2>/dev/null || true)
    h2_count=$(echo "$h2_count" | tr -d '[:space:]')
    h1_count=$(grep -c '^# <img' "$file" 2>/dev/null || true)
    h1_count=$(echo "$h1_count" | tr -d '[:space:]')

    local count=0
    [ -n "$h2_count" ] && [ "$h2_count" -gt 0 ] 2>/dev/null && count="$h2_count"
    [ "$count" -eq 0 ] && [ -n "$h1_count" ] && [ "$h1_count" -gt 0 ] 2>/dev/null && count="$h1_count"

    if [ "$count" -gt 0 ] 2>/dev/null; then
        echo "$count"
        return
    fi

    # 4. 兜底（无图标标记的单软件文件）
    echo 1
}

count_software() {
    local dir="$1"
    if [ ! -d "$dir" ]; then
        echo "0"
        return
    fi

    local total=0
    while IFS= read -r file; do
        local n
        n=$(count_in_file "$file")
        total=$((total + n))
    done < <(find "$dir" -name "*.md" -type f \
        ! -name "README.md" \
        ! -name "CLAUDE.md" \
        ! -name "test.md" \
        ! -name "config.md" \
        ! -path "*test*" 2>/dev/null)
    echo "$total"
}

# 用新表格替换 README 中对应的表格区块
update_table() {
    local file="$1"
    local header_pattern="$2"
    local new_table_file="$3"

    [ -f "$file" ] || { echo "警告：$file 不存在，跳过"; return; }

    local tmp="${file}.tmp"
    awk -v header="$header_pattern" -v ntf="$new_table_file" '
        BEGIN { in_table = 0; replaced = 0 }
        !replaced && index($0, header) {
            in_table = 1
            while ((getline line < ntf) > 0) print line
            close(ntf)
            replaced = 1
            next
        }
        in_table && /^\|/ { next }
        { in_table = 0; print }
    ' "$file" > "$tmp" && mv "$tmp" "$file"
}

echo ""
echo "注：在 Git Bash (Windows) 下运行较慢属正常现象，每个文件需启动多个子进程（grep/sed/head），"
echo "    Windows 的 fork 开销远高于 Linux，数十个文件累积后耗时十几秒属预期范围。"


# 收集各平台数据
counts_file=$(mktemp)
grand_total=0
for platform in Windows Linux MacOS General Android iOS; do
    ess=$(count_software "$platform/Essential")
    opt=$(count_software "$platform/Optional")
    sum=$((ess + opt))
    echo "$platform $ess $opt $sum" >> "$counts_file"
    grand_total=$((grand_total + sum))
done

# 打印统计
echo "## 软件收录统计"
echo ""
echo "| 平台 | Essential | Optional | 合计 |"
echo "|------|-----------|----------|------|"
while read -r platform ess opt sum; do
    printf "| %s | %d | %d | **%d** |\n" "$platform" "$ess" "$opt" "$sum"
done < "$counts_file"
echo ""
echo "总计：$grand_total 款软件"
echo ""

# 生成中英文表格临时文件
zh_table=$(mktemp)
en_table=$(mktemp)

{
    echo "| 平台 | Essential | Optional | 合计 |"
    echo "|------|-----------|----------|------|"
    while read -r platform ess opt sum; do
        printf "| %s | %d | %d | **%d** |\n" "$platform" "$ess" "$opt" "$sum"
    done < "$counts_file"
} > "$zh_table"

{
    echo "| Platform | Essential | Optional | Total |"
    echo "|----------|-----------|----------|-------|"
    while read -r platform ess opt sum; do
        printf "| %s | %d | %d | **%d** |\n" "$platform" "$ess" "$opt" "$sum"
    done < "$counts_file"
} > "$en_table"

# 自动写入两个 README
update_table "README_zh.md" "| 平台 | Essential | Optional | 合计 |" "$zh_table"
update_table "README_en.md" "| Platform | Essential | Optional | Total |" "$en_table"

rm -f "$counts_file" "$zh_table" "$en_table"

echo "✓ README_zh.md 和 README_en.md 已更新"
