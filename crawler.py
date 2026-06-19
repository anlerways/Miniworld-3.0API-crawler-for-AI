#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
迷你世界 UGC 3.0 API 爬虫
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import sys
from collections import defaultdict

# ============================================================
# 配置：所有 API 模块
# ============================================================

API_MODULES = {
    "World": "https://dev-wiki.mini1.cn/ugc-wiki/apis/world.html",
    "GameObject": "https://dev-wiki.mini1.cn/ugc-wiki/apis/gameobject.html",
    "Actor": "https://dev-wiki.mini1.cn/ugc-wiki/apis/actor.html",
    "Player": "https://dev-wiki.mini1.cn/ugc-wiki/apis/player.html",
    "Monster": "https://dev-wiki.mini1.cn/ugc-wiki/apis/monster.html",
    "Block": "https://dev-wiki.mini1.cn/ugc-wiki/apis/block.html",
    "Item": "https://dev-wiki.mini1.cn/ugc-wiki/apis/item.html",
    "Backpack": "https://dev-wiki.mini1.cn/ugc-wiki/apis/backpack.html",
    "CustomUI": "https://dev-wiki.mini1.cn/ugc-wiki/apis/customui.html",
    "Graphics": "https://dev-wiki.mini1.cn/ugc-wiki/apis/graphics.html",
    "Area": "https://dev-wiki.mini1.cn/ugc-wiki/apis/area.html",
    "WorldContainer": "https://dev-wiki.mini1.cn/ugc-wiki/apis/worldcontainer.html",
    "Mod": "https://dev-wiki.mini1.cn/ugc-wiki/apis/mod.html",
    "Timer": "https://dev-wiki.mini1.cn/ugc-wiki/apis/timer.html",
    "Buff": "https://dev-wiki.mini1.cn/ugc-wiki/apis/buff.html",
    "Chat": "https://dev-wiki.mini1.cn/ugc-wiki/apis/chat.html",
    "Data": "https://dev-wiki.mini1.cn/ugc-wiki/apis/data.html",
    "Array": "https://dev-wiki.mini1.cn/ugc-wiki/apis/array.html",
    "Table": "https://dev-wiki.mini1.cn/ugc-wiki/apis/table.html",
    "Map": "https://dev-wiki.mini1.cn/ugc-wiki/apis/map.html",
}

# ============================================================
# 进度条工具
# ============================================================

def print_progress_bar(iteration, total, prefix='', suffix='', length=40, fill='#'):
    """
    在控制台打印进度条
    :param iteration: 当前进度（从0开始）
    :param total: 总步数
    :param prefix: 前缀文字
    :param suffix: 后缀文字
    :param length: 进度条长度（字符数）
    :param fill: 填充字符
    """
    percent = 100 * (iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent:.1f}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        print()  # 换行

# ============================================================
# 网络请求（纯文本日志）
# ============================================================

def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.encoding = "utf-8"
        if resp.status_code == 200:
            return resp.text
        else:
            print(f"  [WARN] 状态码 {resp.status_code}: {url}")
            return None
    except Exception as e:
        print(f"  [ERROR] 请求失败: {url} - {e}")
        return None

# ============================================================
# API 函数解析（只提取描述、参数、返回值）
# ============================================================

def parse_api_functions(html, module_name):
    soup = BeautifulSoup(html, "html.parser")
    functions = []
    func_map = {}
    anchor_to_name = {}

    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 3:
                name_cell = cells[1]
                link = name_cell.find("a")
                if link:
                    func_name = link.get_text(strip=True)
                    anchor = link.get("href", "").replace("#", "")
                else:
                    func_name = name_cell.get_text(strip=True)
                    anchor = ""
                desc = cells[2].get_text(strip=True) if len(cells) > 2 else ""
                if func_name in ["函数名", "序号", "方法名", "函数描述"]:
                    continue
                if func_name:
                    clean_name = re.sub(r'\(.*\)$', '', func_name).strip()
                    func_map[clean_name] = {"description": desc, "anchor": anchor}
                    if anchor:
                        anchor_to_name[anchor] = clean_name

    detail_blocks = {}
    for header in soup.find_all(["h2", "h3", "h4"]):
        func_name = header.get_text(strip=True)
        clean_name = re.sub(r'\(.*\)$', '', func_name).strip()
        if not clean_name or len(clean_name) < 2:
            continue

        header_id = header.get("id") or header.get("name")
        if header_id and header_id in anchor_to_name:
            key = anchor_to_name[header_id]
        else:
            key = clean_name

        detail = extract_detail_from_header(header)
        if detail:
            detail_blocks[key] = detail

    for func_name, info in func_map.items():
        detail = detail_blocks.get(func_name, {})
        if info["description"] and not detail.get("description"):
            detail["description"] = info["description"]
        functions.append({
            "module": module_name,
            "name": func_name,
            "description": detail.get("description", ""),
            "params": detail.get("params", []),
            "returns": detail.get("returns", []),
        })

    if not functions:
        for name, detail in detail_blocks.items():
            functions.append({
                "module": module_name,
                "name": name,
                "description": detail.get("description", ""),
                "params": detail.get("params", []),
                "returns": detail.get("returns", []),
            })

    return functions


def extract_detail_from_header(header):
    detail = {"params": [], "returns": [], "description": ""}

    siblings = []
    sibling = header.find_next_sibling()
    while sibling and sibling.name not in ["h1", "h2", "h3", "h4", "h5"]:
        siblings.append(sibling)
        sibling = sibling.find_next_sibling()

    for node in siblings:
        if node.name == "p" and len(node.get_text(strip=True)) > 5:
            detail["description"] = node.get_text(strip=True)
            break

    for node in siblings:
        if node.name == "ul":
            for li in node.find_all("li", recursive=False):
                text = li.get_text(strip=True)
                if "参数及类型" in text:
                    sub_ul = li.find("ul")
                    if sub_ul:
                        for sub_li in sub_ul.find_all("li"):
                            param_text = sub_li.get_text(separator=" ", strip=True)
                            m = re.match(r'([a-zA-Z_]\w*)\s*[:：]\s*([^\s]+(?:\s*/\s*[^\s]+)?)\s*(.*)', param_text)
                            if m:
                                detail["params"].append({
                                    "name": m.group(1).strip(),
                                    "type": m.group(2).strip(),
                                    "desc": m.group(3).strip()
                                })
                            else:
                                parts = param_text.split(maxsplit=1)
                                if len(parts) == 2:
                                    detail["params"].append({
                                        "name": parts[0].strip(),
                                        "type": "",
                                        "desc": parts[1].strip()
                                    })
                        break

    for node in siblings:
        if node.name == "ul":
            for li in node.find_all("li", recursive=False):
                text = li.get_text(strip=True)
                if "返回值及类型" in text:
                    sub_ul = li.find("ul")
                    if sub_ul:
                        for sub_li in sub_ul.find_all("li"):
                            ret_text = sub_li.get_text(separator=" ", strip=True)
                            m = re.match(r'([a-zA-Z_]\w*)\s*[:：]\s*([^\s]+(?:\s*/\s*[^\s]+)?)\s*(.*)', ret_text)
                            if m:
                                detail["returns"].append({
                                    "name": m.group(1).strip(),
                                    "type": m.group(2).strip(),
                                    "desc": m.group(3).strip()
                                })
                            else:
                                detail["returns"].append({
                                    "name": "",
                                    "type": "",
                                    "desc": ret_text
                                })
                        break

    return detail

# ============================================================
# 枚举解析
# ============================================================

def parse_enums_from_page(html):
    soup = BeautifulSoup(html, "html.parser")
    enums = {}

    for table in soup.find_all("table"):
        enum_name = "Misc"
        prev = table.find_previous(["h1", "h2", "h3", "h4"])
        if prev:
            title = prev.get_text(strip=True)
            name_match = re.search(r'([A-Za-z_]\w+)', title)
            if name_match:
                enum_name = name_match.group(1)
            else:
                enum_name = title.strip()

        rows = table.find_all("tr")
        for row in rows[1:]:
            cells = row.find_all("td")
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True)
                val = cells[1].get_text(strip=True)
                if key in ["名称", "常量", "用法描述"]:
                    continue
                if "." in key:
                    e_name, const = key.split(".", 1)
                    enums.setdefault(e_name, {})[const] = val
                else:
                    enums.setdefault(enum_name, {})[key] = val

    return enums

# ============================================================
# 生成 Markdown 输出
# ============================================================

def generate_full_md(all_functions):
    lines = ["# 《迷你世界》UGC 3.0 API 参考手册\n"]
    lines.append("> GitHub开源仓库: https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI\n")
    lines.append("> 本文档由爬虫自动生成，数据来源：https://dev-wiki.mini1.cn/ugc-wiki/\n")

    by_module = defaultdict(list)
    for func in all_functions:
        by_module[func["module"]].append(func)

    for module, funcs in sorted(by_module.items()):
        lines.append(f"\n## {module}\n")
        for func in sorted(funcs, key=lambda x: x["name"]):
            lines.append(f"### `{func['name']}`\n")
            if func.get("description"):
                lines.append(f"**描述**: {func['description']}\n")
            if func.get("params"):
                lines.append("**参数**:\n")
                for p in func["params"]:
                    p_name = p.get("name", "")
                    p_type = p.get("type", "")
                    p_desc = p.get("desc", "")
                    line = f"- `{p_name}`"
                    if p_type:
                        line += f" ({p_type})"
                    if p_desc:
                        line += f" — {p_desc}"
                    lines.append(line + "\n")
            if func.get("returns"):
                lines.append("**返回值**:\n")
                for r in func["returns"]:
                    r_name = r.get("name", "")
                    r_type = r.get("type", "")
                    r_desc = r.get("desc", "")
                    line = f"- `{r_name}`"
                    if r_type:
                        line += f" ({r_type})"
                    if r_desc:
                        line += f" — {r_desc}"
                    lines.append(line + "\n")
            lines.append("\n---\n")
    return "".join(lines)


def generate_summary_md(all_functions):
    lines = ["# 《迷你世界》UGC 3.0 API 速查表\n"]
    lines.append("> GitHub开源仓库: https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI\n")
    lines.append("> 仅含函数名和描述，用于快速查阅需要配合VSCode插件使用。\n")
    lines.append("| 模块 | 函数名 | 描述 |\n")
    lines.append("|------|--------|------|\n")
    for func in sorted(all_functions, key=lambda x: (x["module"], x["name"])):
        name = func["name"]
        desc = func.get("description", "").replace("|", "\\|")
        lines.append(f"| {func['module']} | `{name}` | {desc} |\n")
    return "".join(lines)

    
def generate_enum_md(enums):
    lines = ["# 《迷你世界》UGC 3.0 枚举参考手册\n"]
    lines.append("> GitHub开源仓库: https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI\n")
    lines.append("> 本文档由爬虫自动生成，数据来源：https://dev-wiki.mini1.cn/ugc-wiki/\n")

    if not enums:
        lines.append("⚠️ 未提取到任何枚举常量。\n")
        return "".join(lines)

    for enum_name, consts in sorted(enums.items()):
        lines.append(f"\n## {enum_name}\n")
        for const, value in sorted(consts.items()):
            lines.append(f"- `{const}` = {value}\n")
    return "".join(lines)

# ============================================================
# 主程序
# ============================================================

def main():
    print("=" * 70)
    print("迷你世界 UGC 3.0 API 爬虫")
    print("BY TEMP AXIS")
    print("GitHub开源仓库: https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI")
    print("请勿用于任何非法用途，仅供学习和参考！")
    print("本资源完全开源免费，如果你收费得到的，那么你被骗了")
    print("VSCode插件下载地址https://dev-wiki.mini1.cn/cyclopdeia?wikiMenuId=3&wikiId=2324")
    print(f"共 {len(API_MODULES)} 个模块")
    print("=" * 70)

    # ---- 询问输出模式 ----
    print("\n请选择输出模式：")
    print("  1 - 完整版（含参数、返回值）")
    print("  2 - 精简版（仅函数名 + 描述）配合 VSCode 插件使用")
    print("  3 - 同时生成完整版和精简版")
    choice = input("请输入数字（1/2/3）: ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("输入无效，请重新选择（1/2/3）: ").strip()

    generate_full = choice in ["1", "3"]
    generate_summary = choice in ["2", "3"]

    # ---- 爬取 API 模块（带进度条） ----
    all_functions = []
    total_modules = len(API_MODULES)
    print("\n[INFO] 开始爬取 API 模块...")
    for idx, (module_name, url) in enumerate(API_MODULES.items(), 1):
        # 更新进度条
        print_progress_bar(idx - 1, total_modules, prefix='Progress', suffix=f'({idx-1}/{total_modules})', length=40)
        html = fetch_html(url)
        if html:
            funcs = parse_api_functions(html, module_name)
            all_functions.extend(funcs)
            # 打印提取到的函数数量（在进度条下方另起一行）
            sys.stdout.write(f'\r[INFO] {module_name}: 提取到 {len(funcs)} 个函数\n')
        else:
            sys.stdout.write(f'\r[WARN] {module_name}: 页面无法访问，已跳过\n')
        time.sleep(0.5)
    # 完成进度
    print_progress_bar(total_modules, total_modules, prefix='Progress', suffix='(完成)', length=40)

    print(f"\n[INFO] 总计提取到 {len(all_functions)} 个 API 函数")

    # ---- 爬取枚举（仅 global.html） ----
    print("\n[INFO] 正在爬取枚举库 (global.html) ...")
    enum_html = fetch_html("https://dev-wiki.mini1.cn/ugc-wiki/apis/global.html")
    enums = {}
    if enum_html:
        enums = parse_enums_from_page(enum_html)
        total = sum(len(c) for c in enums.values())
        print(f"[INFO] 提取到 {len(enums)} 个枚举组，共 {total} 个常量")
    else:
        print("[ERROR] 枚举页面获取失败")

    # ---- 生成 Markdown 文件 ----
    print("\n[INFO] 生成 Markdown 文档...")

    if generate_full:
        with open("api_reference.md", "w", encoding="utf-8") as f:
            f.write(generate_full_md(all_functions))
        print("  [OK] api_reference.md（完整版）")

    if generate_summary:
        with open("api_summary.md", "w", encoding="utf-8") as f:
            f.write(generate_summary_md(all_functions))
        print("  [OK] api_summary.md（精简版）")

    # 枚举始终生成
    with open("enum_reference.md", "w", encoding="utf-8") as f:
        f.write(generate_enum_md(enums))
    print("  [OK] enum_reference.md（枚举）")

    print("\n[OK] 爬取完成！")
    if generate_full:
        print(f"  - 完整 API 函数: {len(all_functions)} 个")
    if generate_summary:
        print(f"  - 精简 API 函数: {len(all_functions)} 个（仅名称+描述）")
    print(f"  - 枚举常量: {sum(len(c) for c in enums.values())} 个")

if __name__ == "__main__":
    main()