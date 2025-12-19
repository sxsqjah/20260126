#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Frame, PageTemplate
from reportlab.platypus.flowables import Image
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

# 创建PDF文档
output_file = 'Crypto-K_Quants_Whitepaper_v1.3.pdf'
doc = SimpleDocTemplate(output_file, pagesize=A4,
                       rightMargin=2*cm, leftMargin=2*cm,
                       topMargin=2*cm, bottomMargin=2*cm)

# 创建样式
styles = getSampleStyleSheet()

# 自定义样式
section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a1a2e'),
    spaceAfter=20,
    spaceBefore=30,
    alignment=TA_LEFT,
    fontName='Helvetica-Bold'
)

subsection_style = ParagraphStyle(
    'Subsection',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=colors.HexColor('#16213e'),
    spaceAfter=12,
    spaceBefore=20,
    alignment=TA_LEFT,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#0f0f0f'),
    spaceAfter=12,
    alignment=TA_JUSTIFY,
    fontName='Helvetica',
    leading=16
)

disclaimer_style = ParagraphStyle(
    'Disclaimer',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#666666'),
    spaceAfter=15,
    alignment=TA_JUSTIFY,
    fontName='Helvetica-Oblique',
    leading=14
)

# 构建内容
story = []

def add_paragraph(text, style):
    """添加段落"""
    if text.strip():
        story.append(Paragraph(text.replace('\n', '<br/>'), style))
        story.append(Spacer(1, 0.2*cm))

def add_section(text):
    """添加章节标题"""
    story.append(PageBreak())
    add_paragraph(text, section_title_style)

def add_subsection(text):
    """添加小节标题"""
    add_paragraph(text, subsection_style)

# ========== 封面页函数 ==========
def create_cover_page(canvas_obj, doc):
    """创建带背景的封面"""
    # 绘制背景渐变
    width, height = A4
    
    # 使用更高效的渐变绘制方法（分块绘制）
    num_steps = 100  # 减少绘制次数
    step_height = height / num_steps
    for i in range(num_steps):
        ratio = i / num_steps
        # 从深蓝到浅蓝的渐变
        r = int(26 + (22 - 26) * ratio)
        g = int(26 + (33 - 26) * ratio)
        b = int(46 + (62 - 46) * ratio)
        canvas_obj.setFillColorRGB(r/255, g/255, b/255)
        canvas_obj.rect(0, height - (i + 1) * step_height, width, step_height, fill=1, stroke=0)
    
    # 绘制装饰性几何图形
    canvas_obj.setFillColorRGB(0.1, 0.2, 0.3)
    canvas_obj.setStrokeColorRGB(0.15, 0.25, 0.35)
    canvas_obj.setLineWidth(2)
    
    # 绘制一些圆形装饰
    for i in range(3):
        x = width * (0.2 + i * 0.3)
        y = height * (0.3 + i * 0.1)
        radius = 50 + i * 30
        canvas_obj.setFillAlpha(0.1)
        canvas_obj.setStrokeAlpha(0.3)
        canvas_obj.circle(x, y, radius, fill=1, stroke=1)
    
    # 绘制网格线
    canvas_obj.setStrokeColorRGB(0.2, 0.3, 0.4)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.setStrokeAlpha(0.1)
    for i in range(0, int(width), 50):
        canvas_obj.line(i, 0, i, height)
    for i in range(0, int(height), 50):
        canvas_obj.line(0, i, width, i)
    
    # 重置透明度
    canvas_obj.setFillAlpha(1.0)
    canvas_obj.setStrokeAlpha(1.0)
    
    # 添加标题文字
    canvas_obj.saveState()
    canvas_obj.setFillColorRGB(1, 1, 1)  # 白色文字
    
    # 主标题
    canvas_obj.setFont("Helvetica-Bold", 48)
    title_text = "Crypto-K Quants"
    text_width = canvas_obj.stringWidth(title_text, "Helvetica-Bold", 48)
    canvas_obj.drawString((width - text_width) / 2, height * 0.6, title_text)
    
    # 副标题
    canvas_obj.setFont("Helvetica", 32)
    subtitle_text = "Whitepaper"
    text_width = canvas_obj.stringWidth(subtitle_text, "Helvetica", 32)
    canvas_obj.drawString((width - text_width) / 2, height * 0.5, subtitle_text)
    
    # 版本号
    canvas_obj.setFont("Helvetica-Oblique", 20)
    version_text = "Version 1.3"
    text_width = canvas_obj.stringWidth(version_text, "Helvetica-Oblique", 20)
    canvas_obj.drawString((width - text_width) / 2, height * 0.35, version_text)
    
    # 底部装饰线
    canvas_obj.setStrokeColorRGB(0.8, 0.8, 0.8)
    canvas_obj.setLineWidth(2)
    canvas_obj.line(width * 0.2, height * 0.2, width * 0.8, height * 0.2)
    
    canvas_obj.restoreState()

def create_normal_page(canvas_obj, doc):
    """创建普通内容页"""
    canvas_obj.saveState()
    # 可以在这里添加页眉页脚等
    canvas_obj.restoreState()

# ========== 内容开始 ==========
# 添加封面后，内容从第二页开始
story.append(PageBreak())

# ========== I. 英文版本 ==========
add_section("I. English Version")

add_subsection("Disclaimer")
add_paragraph(
    "This whitepaper is for informational purposes only and does not constitute investment advice, "
    "financial advice, trading advice, or any form of solicitation. Cryptocurrency markets are highly "
    "volatile and involve substantial risk. Users are solely responsible for their trading decisions "
    "and potential losses.",
    disclaimer_style
)
add_paragraph(
    "Crypto-K Quants does not guarantee profits, fixed returns, or specific performance outcomes.",
    disclaimer_style
)

add_subsection("1. Executive Summary")
add_paragraph(
    "Crypto-K Quants is a quantitative research and execution team focused on cryptocurrency markets. "
    "Our objective is to apply institution-grade quantitative methodologies, risk control frameworks, "
    "and automated execution systems to the highly volatile and noise-driven crypto environment.",
    body_style
)
add_paragraph(
    "Rather than attempting to predict market direction, Crypto-K Quants is designed to manage uncertainty "
    "through probability-based models, disciplined execution, and strict drawdown control.",
    body_style
)

add_subsection("2. Market Background")
add_paragraph(
    "Cryptocurrency markets exhibit several structural characteristics:",
    body_style
)
add_paragraph("• Extreme volatility", body_style)
add_paragraph("• 24/7 trading without circuit breakers", body_style)
add_paragraph("• High leverage availability", body_style)
add_paragraph("• Strong emotional participation by retail traders", body_style)
add_paragraph(
    "Most retail losses are not caused by a lack of opportunities, but by the absence of systematic execution, "
    "risk discipline, and long-term statistical thinking.",
    body_style
)

add_subsection("3. Our Approach")
add_paragraph(
    "Crypto-K Quants is built on three core principles:",
    body_style
)
add_paragraph("• Systems over discretion", body_style)
add_paragraph("• Risk control before return optimization", body_style)
add_paragraph("• Long-term statistical validity over short-term performance", body_style)
add_paragraph(
    "Our services are designed to be transparent, repeatable, and auditable.",
    body_style
)

add_subsection("4. System Architecture")
add_paragraph("4.1 Data Layer", body_style)
add_paragraph("• Multi-timeframe price data", body_style)
add_paragraph("• Volume and volatility metrics", body_style)
add_paragraph("• Derived statistical factors", body_style)
add_paragraph("• Market regime classification", body_style)

add_paragraph("4.2 Model Layer", body_style)
add_paragraph("• K-Model: Multi-timeframe resonance analysis", body_style)
add_paragraph("• DL-Signal Engine: Noise filtering and false breakout detection", body_style)
add_paragraph("• Risk Engine: Drawdown budgeting and exposure control", body_style)

add_paragraph("4.3 Execution Layer", body_style)
add_paragraph("• Smart order routing", body_style)
add_paragraph("• Slippage monitoring", body_style)
add_paragraph("• Exchange API protection mechanisms", body_style)

add_subsection("5. Strategy Framework")
add_paragraph(
    "Crypto-K Quants strategies are categorized by structure and risk profile:",
    body_style
)
add_paragraph("• Trend-following strategies", body_style)
add_paragraph("• Breakout strategies with confirmation filters", body_style)
add_paragraph("• Volatility-aware systematic strategies", body_style)
add_paragraph(
    "No strategy relies on martingale, unlimited averaging, or discretionary overrides.",
    body_style
)

add_subsection("6. Risk Management")
add_paragraph(
    "Risk control is enforced at multiple levels:",
    body_style
)
add_paragraph("• Per-trade risk limits", body_style)
add_paragraph("• Strategy-level drawdown caps", body_style)
add_paragraph("• Account-level exposure limits", body_style)
add_paragraph("• Automatic risk reduction during extreme market conditions", body_style)
add_paragraph(
    "Preserving capital is treated as a prerequisite for long-term participation.",
    body_style
)

add_subsection("7. Product Offering")
add_paragraph("• Strategy subscription services", body_style)
add_paragraph("• Automated copy-trading via API", body_style)
add_paragraph("• Signal delivery via Telegram and API", body_style)
add_paragraph("• Professional access for advanced users", body_style)
add_paragraph(
    "Users retain full control over their accounts at all times.",
    body_style
)

add_subsection("8. Business Model")
add_paragraph("• Subscription-based pricing", body_style)
add_paragraph("• Tiered access by strategy and risk profile", body_style)
add_paragraph("• Optional performance-based fees for qualified users", body_style)
add_paragraph("• Custom and white-label solutions for institutions", body_style)

add_subsection("9. Roadmap")
add_paragraph("• Expansion of strategy universe", body_style)
add_paragraph("• Enhanced deep-learning signal modules", body_style)
add_paragraph("• Multi-exchange infrastructure", body_style)
add_paragraph("• Institutional deployment and compliance enhancements", body_style)

add_subsection("10. Conclusion")
add_paragraph(
    "Crypto-K Quants is not designed to chase short-term performance. "
    "It is designed to survive, adapt, and compound over time through discipline "
    "and probability-driven decision-making.",
    body_style
)

# ========== II. 韩文版本 ==========
add_section("II. Korean Version (한국어)")

add_subsection("면책 조항")
add_paragraph(
    "본 백서는 정보 제공 목적이며 투자 권유, 재무 자문 또는 수익 보장을 의미하지 않습니다. "
    "암호화폐 거래는 높은 변동성과 위험을 수반하며, 모든 거래 결정과 손실에 대한 책임은 사용자 본인에게 있습니다.",
    disclaimer_style
)

add_subsection("1. 개요")
add_paragraph(
    "Crypto-K Quants는 암호화폐 시장에 특화된 정량적(퀀트) 연구 및 자동 실행 팀입니다. "
    "우리는 예측이 아닌 확률과 리스크 관리에 기반한 시스템 트레이딩을 지향합니다.",
    body_style
)

add_subsection("2. 시장 환경")
add_paragraph(
    "암호화폐 시장의 구조적 특징:",
    body_style
)
add_paragraph("• 극심한 변동성", body_style)
add_paragraph("• 24시간 거래", body_style)
add_paragraph("• 높은 레버리지 접근성", body_style)
add_paragraph("• 감정 기반 거래 비중이 높음", body_style)
add_paragraph(
    "대부분의 손실은 기회 부족이 아니라 시스템 부재에서 발생합니다.",
    body_style
)

add_subsection("3. 핵심 원칙")
add_paragraph("• 감각보다 시스템", body_style)
add_paragraph("• 수익보다 리스크 관리", body_style)
add_paragraph("• 단기 성과보다 장기 통계", body_style)

add_subsection("4. 기술 구조")
add_paragraph("• 데이터 계층", body_style)
add_paragraph("• 다중 주기 공진 모델(K-Model)", body_style)
add_paragraph("• 딥러닝 기반 신호 필터", body_style)
add_paragraph("• 자동 실행 및 리스크 엔진", body_style)

add_subsection("5. 전략 구조")
add_paragraph("• 추세 추종 전략", body_style)
add_paragraph("• 확인 필터 기반 돌파 전략", body_style)
add_paragraph("• 변동성 인지형 시스템 전략", body_style)
add_paragraph(
    "무한 물타기나 마틴게일 전략은 사용하지 않습니다.",
    body_style
)

add_subsection("6. 리스크 관리")
add_paragraph("• 거래 단위 리스크 제한", body_style)
add_paragraph("• 전략별 최대 손실 제한", body_style)
add_paragraph("• 계좌 단위 노출 관리", body_style)
add_paragraph("• 극단적 시장 상황 자동 보호", body_style)

add_subsection("7. 서비스 형태")
add_paragraph("• 전략 구독", body_style)
add_paragraph("• API 기반 자동 매매", body_style)
add_paragraph("• 텔레그램 신호 제공", body_style)
add_paragraph("• 전문 사용자 인터페이스", body_style)

add_subsection("8. 비즈니스 모델")
add_paragraph("• 구독 기반", body_style)
add_paragraph("• 단계별 접근 권한", body_style)
add_paragraph("• 조건부 성과 수수료", body_style)
add_paragraph("• 기관 맞춤 솔루션", body_style)

add_subsection("9. 향후 계획")
add_paragraph("• 전략 확장", body_style)
add_paragraph("• 모델 고도화", body_style)
add_paragraph("• 다중 거래소 지원", body_style)
add_paragraph("• 기관 협업 확대", body_style)

add_subsection("10. 결론")
add_paragraph(
    "Crypto-K Quants는 단기 수익을 약속하지 않습니다. "
    "우리는 시장에서 오래 살아남는 시스템을 구축합니다.",
    body_style
)

# ========== III. 中文版本 ==========
add_section("III. 中文版本（简体中文）")

add_subsection("免责声明")
add_paragraph(
    "本白皮书仅用于项目说明，不构成任何投资、理财或收益承诺。 "
    "加密资产交易风险极高，用户需自行承担全部交易风险。",
    disclaimer_style
)

add_subsection("1. 项目概述")
add_paragraph(
    "Crypto-K Quants 是专注于加密货币市场的量化研究与自动化执行团队。 "
    "我们不以预测市场为目标，而是通过概率模型与风险管理实现长期稳定运作。",
    body_style
)

add_subsection("2. 市场背景")
add_paragraph(
    "加密市场长期存在以下问题：",
    body_style
)
add_paragraph("• 高波动", body_style)
add_paragraph("• 高杠杆", body_style)
add_paragraph("• 情绪化交易普遍", body_style)
add_paragraph("• 系统化交易能力不足", body_style)
add_paragraph(
    "多数亏损源于缺乏纪律，而非缺乏机会。",
    body_style
)

add_subsection("3. 核心理念")
add_paragraph("• 系统优先", body_style)
add_paragraph("• 风控优先", body_style)
add_paragraph("• 长期统计优先", body_style)

add_subsection("4. 技术架构")
add_paragraph("• 数据层", body_style)
add_paragraph("• 多周期共振模型（K-Model）", body_style)
add_paragraph("• 深度学习信号引擎", body_style)
add_paragraph("• 自动执行与风控系统", body_style)

add_subsection("5. 策略体系")
add_paragraph("• 趋势策略", body_style)
add_paragraph("• 突破策略", body_style)
add_paragraph("• 变动率感知策略", body_style)
add_paragraph(
    "不使用马丁格尔、不无限补仓。",
    body_style
)

add_subsection("6. 风险管理")
add_paragraph("• 单笔风险限制", body_style)
add_paragraph("• 策略级回撤控制", body_style)
add_paragraph("• 账户级风险预算", body_style)
add_paragraph("• 极端行情自动保护", body_style)

add_subsection("7. 产品形式")
add_paragraph("• 策略订阅", body_style)
add_paragraph("• API 跟单", body_style)
add_paragraph("• 信号推送", body_style)
add_paragraph("• 专业接口", body_style)

add_subsection("8. 商业模式")
add_paragraph("• 订阅制", body_style)
add_paragraph("• 分级收费", body_style)
add_paragraph("• 可选成果分成", body_style)
add_paragraph("• 定制与白标方案", body_style)

add_subsection("9. 发展规划")
add_paragraph("• 策略扩展", body_style)
add_paragraph("• 模型升级", body_style)
add_paragraph("• 多交易所支持", body_style)
add_paragraph("• 机构级部署", body_style)

add_subsection("10. 结语")
add_paragraph(
    "Crypto-K Quants 不制造神话，只构建可长期存活的交易系统。",
    body_style
)

# ========== IV. 日文版本 ==========
add_section("IV. Japanese Version（日本語）")

add_subsection("免責事項")
add_paragraph(
    "本ホワイトペーパーは情報提供のみを目的としており、投資助言や利益保証を行うものではありません。 "
    "暗号資産取引には高いリスクが伴い、すべての責任は利用者自身に帰属します。",
    disclaimer_style
)

add_subsection("1. 概要")
add_paragraph(
    "Crypto-K Quants は暗号資産市場に特化したクオンツ研究および自動売買チームです。 "
    "市場予測ではなく、確率とリスク管理を重視します。",
    body_style
)

add_subsection("2. 市場背景")
add_paragraph("• 高いボラティリティ", body_style)
add_paragraph("• 24時間取引", body_style)
add_paragraph("• 高レバレッジ", body_style)
add_paragraph("• 感情的取引が多い", body_style)

add_subsection("3. 基本理念")
add_paragraph("• 裁量よりシステム", body_style)
add_paragraph("• 利益よりリスク管理", body_style)
add_paragraph("• 短期より長期", body_style)

add_subsection("4. 技術構成")
add_paragraph("• データ層", body_style)
add_paragraph("• マルチタイムフレーム分析", body_style)
add_paragraph("• ディープラーニング信号", body_style)
add_paragraph("• 自動執行エンジン", body_style)

add_subsection("5. 戦略体系")
add_paragraph("• トレンドフォロー", body_style)
add_paragraph("• ブレイクアウト戦略", body_style)
add_paragraph("• ボラティリティ認識型戦略", body_style)

add_subsection("6. リスク管理")
add_paragraph("• 取引単位の損失制限", body_style)
add_paragraph("• 戦略別ドローダウン管理", body_style)
add_paragraph("• アカウント全体のリスク制御", body_style)

add_subsection("7. 提供サービス")
add_paragraph("• 戦略サブスクリプション", body_style)
add_paragraph("• API 自動売買", body_style)
add_paragraph("• シグナル配信", body_style)
add_paragraph("• プロ向けアクセス", body_style)

add_subsection("8. ビジネスモデル")
add_paragraph("• サブスクリプション", body_style)
add_paragraph("• 段階制料金", body_style)
add_paragraph("• 成果報酬（条件付き）", body_style)
add_paragraph("• 法人向けカスタム対応", body_style)

add_subsection("9. 今後の展開")
add_paragraph("• 戦略拡充", body_style)
add_paragraph("• モデル高度化", body_style)
add_paragraph("• 複数取引所対応", body_style)
add_paragraph("• 機関向け展開", body_style)

add_subsection("10. 結論")
add_paragraph(
    "Crypto-K Quants は短期的な成功を追求しません。 "
    "長期的に生き残る取引システムを構築します。",
    body_style
)

# 构建PDF - 第一页使用封面，其他页面使用普通页面
doc.build(story, onFirstPage=create_cover_page, onLaterPages=create_normal_page)

print(f"PDF文档已生成: {output_file}")
