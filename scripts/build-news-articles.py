#!/usr/bin/env python3
"""Generate static PCSM News article pages and redirect stubs for GitHub Pages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ARTICLES = [
    {
        "slug": "pcsm-wpd-peace-ecosystem-decentralized-technology-for-a-peaceful-and-empowered-future",
        "title": "PCSM-WPD PEACE Ecosystem Decentralized Technology for a Peaceful and Empowered Future",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/ai-generated-8671002_1280-150x150.jpg",
        "excerpt": "How PCSM and the WPD peace ecosystem connect decentralized technology with universal access to basic needs.",
        "paragraphs": [
            "Peaceism connects real-world, value-generating initiatives to a global blockchain ecosystem. PCSM—the Peace Coin for Sustainable Mechanisms—is a BEP-20 token on BNB Smart Chain designed to reward contribution, transparency, and long-term sustainability.",
            "At the center of that vision are seven niches that map to essential human needs: products and services, employment, healthcare, housing and sustainable communities, education, justice and equity, and safety and global resilience. The PCSM–WPD stack is meant to fund, coordinate, and measure progress across those areas with open, auditable rails.",
            "By pairing token incentives with peace-focused programs and community commitment allocations, the ecosystem aims to give every participant a fairer path to prosperity, dignity, and global participation—without relying on closed, extractive intermediaries.",
        ],
        "ctas": [
            ("Explore events by niche", "/pcsm-events/"),
            ("World Commitment Program", "/world-commitment-program/"),
        ],
    },
    {
        "slug": "wpd-node-infrastructure-community-commitment-program",
        "title": "WPD Node Infrastructure & Community Commitment Program",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/blockchain-3019120_1280-150x150.png",
        "excerpt": "How WPD node infrastructure and community commitment programs support a durable peace network.",
        "paragraphs": [
            "World Peace Development (WPD) is the Layer 1 ambition behind Peaceism’s longer-term infrastructure story: a proof-of-stake chain oriented toward secure, stable, and decentralized coordination for peace projects.",
            "Node infrastructure is how that network stays available and accountable. Community operators, validators, and contributors help keep the system online while aligning incentives with public-good outcomes rather than short-term speculation alone.",
            "The Community Commitment Program complements that infrastructure by directing a permanent share of PCSM supply toward vetted charities and peace initiatives—so network growth and real-world impact move together.",
        ],
        "ctas": [
            ("World Commitment Program", "/world-commitment-program/"),
            ("WPD Chain", "/wpd-chain/"),
        ],
    },
    {
        "slug": "world-peace-development-wpd-a-next-generation-blockchain-for-a-secure-stable-and-decentralized-future",
        "title": "World Peace Development (WPD): A Next-Generation Blockchain for a Secure, Stable, and Decentralized Future",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/blockchain-9268421_1280-150x150.png",
        "excerpt": "An overview of WPD—the next-generation blockchain vision for a secure, stable, decentralized future.",
        "paragraphs": [
            "World Peace Development (WPD) is Peaceism’s next-generation blockchain vision: a Layer 1 proof-of-stake network built for secure settlement, stable operation, and decentralized participation.",
            "While PCSM currently operates as a BEP-20 token on BNB Smart Chain, WPD represents the broader infrastructure roadmap—token deployment, analysis tooling, and multi-chain explorer ambitions under a peace-first mandate.",
            "Explore WPD Scan and related resources to follow how the chain is positioned to support transparent value flows for contributors, partners, and public-good programs.",
        ],
        "ctas": [
            ("Open WPD Chain", "/wpd-chain/"),
            ("Read the white paper", "/white-paper/"),
        ],
    },
    {
        "slug": "next-generation-web3-wallet-with-integrated-cold-storage-security",
        "title": "Next-Generation Web3 Wallet with Integrated Cold Storage Security",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/cryptocurrency-7156877_1280-150x150.png",
        "excerpt": "Peaceism’s wallet direction: self-custody UX with stronger cold-storage minded security practices.",
        "paragraphs": [
            "A peace-first token economy only works if people can hold and move assets safely. Peaceism’s wallet direction focuses on practical self-custody: clear portfolio views, transfer and swap flows, and security habits that reduce everyday risk.",
            "Cold-storage minded design means separating hot operational balances from long-term holdings, using hardware or offline key practices where appropriate, and never asking users to surrender seed phrases to a website or chatbot.",
            "Use the PCSM Wallet pages to access exchange and transfer tools, and always verify you are on the official peaceism.io domain before connecting a wallet.",
        ],
        "ctas": [
            ("Open PCSM Wallet", "/wallet/"),
            ("Trade PCSM", "/pcsm-trade/"),
        ],
    },
    {
        "slug": "pcsm-your-gateway-to-the-best-market-rates",
        "title": "PCSM: Your Gateway to the Best Market Rates",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/hand-5815508_1280-150x150.jpg",
        "excerpt": "Why PCSM aims to be a practical gateway for competitive market access across the ecosystem.",
        "paragraphs": [
            "PCSM is built to be useful, not ornamental: a liquid BEP-20 token that can move through trade, rewards, and program participation across the Peaceism ecosystem.",
            "Market access matters because contributors and holders need fair pricing, transparent liquidity, and clear paths to enter or exit positions without opaque intermediaries.",
            "Start from the PCSM Trade page for buy and swap flows, and review Tokenomics for supply, distribution, and the mechanisms that support long-term market health.",
        ],
        "ctas": [
            ("Trade PCSM", "/pcsm-trade/"),
            ("Tokenomics", "/tokenomics/"),
        ],
    },
    {
        "slug": "why-pcsm-is-your-best-choice-for-crypto-swaps",
        "title": "Why PCSM Is Your Best Choice for Crypto Swaps",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/smartphone-5752788_1280-150x150.jpg",
        "excerpt": "What makes PCSM a focused choice for swaps inside the Peaceism market stack.",
        "paragraphs": [
            "Swaps are the everyday bridge between holding PCSM and participating in the wider DeFi surface. Peaceism positions PCSM as the native unit of account for ecosystem activity—trade, rewards, and program access.",
            "Choosing PCSM for swaps keeps activity inside a token economy that publishes its mission, supply framework, and holder programs in the open, instead of scattering value across unrelated meme assets.",
            "Use PCSM Trade and Dexes pages to explore swap paths on BNB Smart Chain, and confirm contract addresses from official Peaceism materials before approving any transaction.",
        ],
        "ctas": [
            ("Swap via PCSM Trade", "/pcsm-trade/"),
            ("View Dexes", "/dexes/"),
        ],
    },
    {
        "slug": "empower-your-crypto-trading-with-pcsms-comprehensive-analysis-tool",
        "title": "Empower Your Crypto Trading with PCSM's Comprehensive Analysis Tool",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/finance-6749717_1280-150x150.jpg",
        "excerpt": "How PCSM Analysis aims to support informed trading with live data and technical context.",
        "paragraphs": [
            "Informed trading needs more than a price ticker. PCSM Analysis is Peaceism’s market intelligence surface—live data, historical context, charts, and technical indicators that help participants read market structure.",
            "The goal is practical clarity: understand momentum, liquidity context, and risk before you size a position, whether you are accumulating PCSM or monitoring related pairs.",
            "Open PCSM Analysis to explore the toolset, and pair it with Tokenomics and the white paper so market decisions stay grounded in the project’s published fundamentals.",
        ],
        "ctas": [
            ("Open PCSM Analysis", "/pcsm-analysis/"),
            ("Buy / Trade PCSM", "/pcsm-trade/"),
        ],
    },
    {
        "slug": "navigating-the-crypto-multiverse-choosing-the-right-blockchain-with-pcsm",
        "title": "Navigating the Crypto Multiverse: Choosing the Right Blockchain with PCSM",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/blockchain-4297721_1280-150x150.jpg",
        "excerpt": "How Peaceism thinks about chain choice—BSC today, WPD as the longer-term infrastructure path.",
        "paragraphs": [
            "The multichain world forces every project to choose where liquidity, security, and users already gather. PCSM launches and trades as a BEP-20 asset on BNB Smart Chain for reach and tooling maturity.",
            "At the same time, Peaceism’s WPD roadmap describes a purpose-built Layer 1 for peace-aligned applications—so chain choice is both a present-tense market decision and a long-term infrastructure bet.",
            "Use WPD Chain resources to follow the L1 path, and keep PCSM activity on official BSC endpoints until migrations or bridges are published by the project.",
        ],
        "ctas": [
            ("Explore WPD Chain", "/wpd-chain/"),
            ("PCSM Tokenomics", "/tokenomics/"),
        ],
    },
    {
        "slug": "pcsm-ai-chatbot-elevating-the-crypto-world-with-artificial-intelligence",
        "title": "PCSM AI Chatbot: Elevating the Crypto World with Artificial Intelligence",
        "date": "July 29, 2025",
        "image": "/wp-content/uploads/2025/07/ai-7977960_1280-150x150.jpg",
        "excerpt": "How Peaceism positions AI assistance and the AI trading bot as tools for informed participation.",
        "paragraphs": [
            "Artificial intelligence can lower the barrier to understanding markets, documentation, and on-chain workflows—when it is used as an assistant, not as an authority that replaces your own verification.",
            "Peaceism’s AI surfaces, including the AI Trading Bot materials, are oriented toward helping users navigate analysis, education, and automation concepts inside the PCSM ecosystem.",
            "Treat every AI suggestion as advisory: confirm contract addresses, fees, and risk yourself. Visit the AI Trading Bot page to learn more about the current product direction.",
        ],
        "ctas": [
            ("AI Trading Bot", "/ai-trading-bot/"),
            ("PCSM Analysis", "/pcsm-analysis/"),
        ],
    },
]

REDIRECTS = [
    ("ai-chatbot", "/ai-trading-bot/"),
    ("crypto-analysis", "/pcsm-analysis/"),
    ("lp-management-program", "/holders-benefits-program/"),
    ("publisher-commitment-program", "/world-commitment-program/"),
    ("pcsm-coins", "/tokenomics/"),
    ("wizard/wizard-coins", "/tokenomics/"),
    ("wizard/wizard-services", "/tokenomics/"),
]

ARTICLE_CSS = """
:root {
  --bg: #f0f5fa;
  --card: #ffffff;
  --text: #334155;
  --heading: #1e293b;
  --accent: #046bd2;
  --accent-hover: #045cb4;
  --muted: #64748b;
  --border: #d1d5db;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.65;
}
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-hover); }
.site-header {
  background: var(--card);
  border-bottom: 1px solid var(--border);
  padding: 1rem 1.25rem;
}
.site-header-inner {
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--heading);
  font-weight: 600;
  font-size: 1.125rem;
}
.brand img { width: 40px; height: 40px; border-radius: 8px; }
.nav-links { display: flex; gap: 1rem; flex-wrap: wrap; font-size: 0.95rem; }
main {
  max-width: 820px;
  margin: 0 auto;
  padding: 2rem 1.25rem 3rem;
}
article {
  background: var(--card);
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.meta {
  color: var(--muted);
  font-size: 0.9rem;
  margin: 0 0 1.25rem;
}
h1 {
  color: var(--heading);
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  line-height: 1.25;
  margin: 0 0 0.75rem;
}
.hero {
  width: 100%;
  max-width: 220px;
  height: auto;
  border-radius: 10px;
  margin: 0 0 1.5rem;
  display: block;
}
article p { margin: 0 0 1rem; }
.cta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.75rem;
}
.btn {
  display: inline-block;
  background: var(--accent);
  color: #fff !important;
  padding: 0.75rem 1.25rem;
  border-radius: 6px;
  font-weight: 500;
}
.btn:hover { background: var(--accent-hover); }
.btn-secondary {
  background: transparent;
  color: var(--accent) !important;
  border: 2px solid var(--accent);
}
.btn-secondary:hover { background: rgba(4,107,210,0.08); }
.site-footer {
  max-width: 820px;
  margin: 0 auto;
  padding: 0 1.25rem 2.5rem;
  color: var(--muted);
  font-size: 0.875rem;
}
"""


def article_html(article: dict) -> str:
    paragraphs = "\n".join(f"      <p>{p}</p>" for p in article["paragraphs"])
    ctas = "\n".join(
        f'      <a class="btn{" btn-secondary" if i else ""}" href="{href}">{label}</a>'
        for i, (label, href) in enumerate(article["ctas"])
    )
    ctas += '\n      <a class="btn btn-secondary" href="/pcsm-news/">Back to PCSM News</a>'
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{article["title"]} &#8211; peaceism</title>
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <meta name="description" content="{article["excerpt"]}">
  <style>{ARTICLE_CSS}</style>
</head>
<body>
  <header class="site-header">
    <div class="site-header-inner">
      <a class="brand" href="/">
        <img src="/pcsm.png" alt="PCSM">
        <span>peaceism</span>
      </a>
      <nav class="nav-links">
        <a href="/pcsm-news/">PCSM News</a>
        <a href="/about-us.html">About Us</a>
        <a href="/white-paper/">White Paper</a>
      </nav>
    </div>
  </header>
  <main>
    <article>
      <p class="meta"><time datetime="2025-07-29">{article["date"]}</time> · PCSM News</p>
      <h1>{article["title"]}</h1>
      <img class="hero" src="{article["image"]}" alt="">
{paragraphs}
      <div class="cta-row">
{ctas}
      </div>
    </article>
  </main>
  <footer class="site-footer">
    <p><strong>Peace</strong> project is a platform which on-boarding real world projects that generate value and health.</p>
    <p>252, Ramkhamhaeng Road, Soi 5, Suan Luang, Bangkok 10250 Thailand · Info@peaceism.org</p>
    <p>©2026. PCSM. All Rights Reserved.</p>
  </footer>
</body>
</html>
"""


def redirect_html(target: str, title: str = "Redirecting…") -> str:
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} &#8211; peaceism</title>
  <link rel="icon" href="/favicon.ico" sizes="any">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
</head>
<body>
  <p>This page has moved. <a href="{target}">Continue here</a>.</p>
  <script>location.replace({target!r});</script>
</body>
</html>
"""


def fix_news_excerpts(news_index: Path) -> None:
    html = news_index.read_text(encoding="utf-8")
    broken = (
        "<p>Home About Us Timeline Platforms AI Trading Bot Crypto Exchange "
        "Create Token Launchpad Create Own Token WPD Blockchain PCSM Token Buy PCSM "
        "PCSM Analysis Tokenomics.</p>"
    )
    for article in ARTICLES:
        old_block = (
            f'<a href="/{article["slug"]}/">\n'
            # match not required for whole block; do title-scoped replace after each title
        )
        # Replace excerpt that follows each article title
        marker = f'<h2 class="ha-post-list-title">{article["title"].replace("&", "&amp;").replace("\'", "&#039;")}</h2>'
        # titles in HTML use &amp; and &#039; already for some
        title_variants = {
            article["title"],
            article["title"].replace("&", "&amp;"),
            article["title"].replace("'", "&#039;"),
            article["title"].replace("&", "&amp;").replace("'", "&#039;"),
        }
        for title in title_variants:
            h2 = f'<h2 class="ha-post-list-title">{title}</h2>'
            if h2 not in html:
                continue
            # find excerpt after this h2
            idx = html.find(h2)
            excerpt_start = html.find('<div class="ha-post-list-excerpt">', idx)
            if excerpt_start == -1 or excerpt_start > idx + 2000:
                continue
            p_start = html.find("<p>", excerpt_start)
            p_end = html.find("</p>", p_start)
            if p_start == -1 or p_end == -1:
                continue
            html = html[: p_start + 3] + article["excerpt"] + html[p_end:]
            break
        else:
            # fallback: if broken excerpt still present near slug link
            pass

    # Global fallback if any broken excerpts remain
    if broken in html:
        # Replace in order of articles appearance
        for article in ARTICLES:
            html = html.replace(broken, f"<p>{article['excerpt']}</p>", 1)

    news_index.write_text(html, encoding="utf-8")


def main() -> None:
    for article in ARTICLES:
        out = ROOT / article["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(article_html(article), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))

    for slug, target in REDIRECTS:
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(redirect_html(target), encoding="utf-8")
        print("redirect", out.relative_to(ROOT), "->", target)

    fix_news_excerpts(ROOT / "pcsm-news" / "index.html")
    print("updated pcsm-news/index.html excerpts")


if __name__ == "__main__":
    main()
