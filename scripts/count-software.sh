#!/bin/bash
# 统计仓库中各平台收录的软件数量
# 用法: bash scripts/count-software.sh
#
# 计数规则（按优先级）：
#   1. <!-- software-count: N -->  手动指定（最高优先级）
#   2. 统计 ## <img 标题的数量       多软件文件中带图标的二级标题
#   3. 存在 # <img 标题 → 1          单软件文件带图标的一级标题
#   4. 兜底 → 1                     无图标标记但视为 1 款
# 排除: README.md, CLAUDE.md, test.md

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

    # 2. 统计带图标的 h2/h1 标题数（取较大值，单软件文件通常只有 1 个）
    local h2_count h1_count
    h2_count=$(grep -c '^## <img' "$file" 2>/dev/null || true)
    h2_count=$(echo "$h2_count" | tr -d '[:space:]')
    h1_count=$(grep -c '^# <img' "$file" 2>/dev/null || true)
    h1_count=$(echo "$h1_count" | tr -d '[:space:]')

    # h2 优先（多软件用 ## 分节），h1 兜底（多软件各用 # 标题）
    local count=0
    [ -n "$h2_count" ] && [ "$h2_count" -gt 0 ] 2>/dev/null && count="$h2_count"
    [ "$count" -eq 0 ] && [ -n "$h1_count" ] && [ "$h1_count" -gt 0 ] 2>/dev/null && count="$h1_count"

    if [ "$count" -gt 0 ] 2>/dev/null; then
        echo "$count"
        return
    fi

    # 4. 兜底（无图标的单软件文件）
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
        ! -path "*test*" 2>/dev/null)
    echo "$total"
}

echo "## 软件收录统计"
echo ""
echo "| 平台 | Essential | Optional | 合计 |"
echo "|------|-----------|----------|------|"

grand_total=0
for platform in Windows Linux MacOS General Android iOS; do
    ess=$(count_software "$platform/Essential")
    opt=$(count_software "$platform/Optional")
    sum=$((ess + opt))
    grand_total=$((grand_total + sum))
    printf "| %s | %d | %d | **%d** |\n" "$platform" "$ess" "$opt" "$sum"
done

echo ""
echo "**总计：$grand_total 款软件**"
echo ""
read -p "按任意键退出..." -n 1 -r
