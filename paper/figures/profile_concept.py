import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --- Colors ---
color_traditional = '#2980B9'  # Deep blue
color_agent = '#C0392B'        # Deep red/coral
color_green = '#1E8449'        # Emerald green
color_bg_trad = '#F2F4F4'
color_bg_agent = '#FDEDEC'

# Create a wide 2-panel figure for full-width figure* in LaTeX
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4), dpi=300)

# ============================================================
# LEFT PANEL: Traditional Profiler
# ============================================================
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10.5)
ax1.axis('off')

# Panel Header
ax1.text(5.0, 10.0, 'Traditional Profiler (Code Functions)', ha='center', va='top',
         fontsize=11, fontweight='bold', color='#2C3E50')

# Left Box: Source Code
box_left_1 = FancyBboxPatch((0.2, 3.2), 2.2, 3.2, boxstyle="round,pad=0.1",
                            facecolor=color_traditional, edgecolor='none', alpha=0.9)
ax1.add_patch(box_left_1)
ax1.text(1.3, 4.8, 'Source Code\nFunctions', ha='center', va='center',
         fontsize=9, color='white', fontweight='bold', linespacing=1.3)

# Arrow 1
ax1.annotate('', xy=(3.0, 4.8), xytext=(2.5, 4.8),
             arrowprops=dict(arrowstyle='->', lw=1.8, color=color_traditional))

# Middle Box: Profiler
box_mid_1 = FancyBboxPatch((3.1, 2.2), 3.8, 5.2, boxstyle="round,pad=0.1",
                           facecolor=color_bg_trad, edgecolor=color_traditional, linewidth=1.8)
ax1.add_patch(box_mid_1)
ax1.text(5.0, 6.9, 'perf / pprof / cProfile', ha='center', va='center',
         fontsize=9.5, fontweight='bold', color=color_traditional)

# Metrics list inside middle box
trad_metrics = [
    ('CPU Time', 'ms'),
    ('Memory', 'MB'),
    ('Cache Misses', '%'),
    ('Function Calls', 'count'),
]
for i, (m_name, m_unit) in enumerate(trad_metrics):
    y_pos = 5.9 - i * 0.9
    ax1.text(3.4, y_pos, m_name, ha='left', va='center', fontsize=8.5, color='#2C3E50')
    ax1.text(6.6, y_pos, m_unit, ha='right', va='center', fontsize=8.0, color='#7F8C8D')

# Arrow 2
ax1.annotate('', xy=(7.5, 4.8), xytext=(7.0, 4.8),
             arrowprops=dict(arrowstyle='->', lw=1.8, color=color_traditional))

# Right Box: Performance Report
box_right_1 = FancyBboxPatch((7.6, 3.2), 2.2, 3.2, boxstyle="round,pad=0.1",
                             facecolor=color_traditional, edgecolor='none', alpha=0.9)
ax1.add_patch(box_right_1)
ax1.text(8.7, 4.8, 'Resource\nReport', ha='center', va='center',
         fontsize=9, color='white', fontweight='bold', linespacing=1.3)

# Bottom note
ax1.text(5.0, 0.9, '[X] Does NOT measure task correctness', ha='center', va='center',
         fontsize=8.5, color='#C0392B', fontweight='bold')


# ============================================================
# RIGHT PANEL: AgentProfiler
# ============================================================
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10.5)
ax2.axis('off')

# Panel Header
ax2.text(5.0, 10.0, 'AgentProfiler (Autonomous Agents)', ha='center', va='top',
         fontsize=11, fontweight='bold', color='#2C3E50')

# Left Box: Autonomous Agent
box_left_2 = FancyBboxPatch((0.2, 4.0), 2.2, 2.8, boxstyle="round,pad=0.1",
                            facecolor=color_agent, edgecolor='none', alpha=0.9)
ax2.add_patch(box_left_2)
ax2.text(1.3, 5.4, 'Autonomous\nAgent', ha='center', va='center',
         fontsize=9, color='white', fontweight='bold', linespacing=1.3)

# Arrow 1
ax2.annotate('', xy=(3.0, 5.4), xytext=(2.5, 5.4),
             arrowprops=dict(arrowstyle='->', lw=1.8, color=color_agent))

# Middle Box: AgentProfiler
box_mid_2 = FancyBboxPatch((3.1, 1.5), 3.8, 7.2, boxstyle="round,pad=0.1",
                           facecolor=color_bg_agent, edgecolor=color_agent, linewidth=1.8)
ax2.add_patch(box_mid_2)
ax2.text(5.0, 8.3, 'AgentProfiler', ha='center', va='center',
         fontsize=10, fontweight='bold', color=color_agent)

# --- Section 1: Declared Budgets ---
ax2.text(3.3, 7.7, 'Declared Budgets:', ha='left', va='center',
         fontsize=8, fontweight='bold', color=color_green)

budgets = [
    ('CPU', '2-4 cores'),
    ('Memory', '4-8 GB'),
    ('Time', '120-600 s'),
    ('Network', 'on / off'),
]
for i, (b_name, b_val) in enumerate(budgets):
    y_pos = 7.25 - i * 0.42
    ax2.text(3.5, y_pos, b_name, ha='left', va='center', fontsize=7.2, color='#2C3E50')
    ax2.text(6.6, y_pos, b_val, ha='right', va='center', fontsize=7.2, color='#7F8C8D')

# Dashed line separator
ax2.plot([3.3, 6.7], [5.6, 5.6], color=color_agent, linestyle='--', linewidth=0.8, alpha=0.7)

# --- Section 2: Measured Profile ---
ax2.text(3.3, 5.25, 'Measured Profile:', ha='left', va='center',
         fontsize=8, fontweight='bold', color=color_agent)

agent_metrics = [
    ('Correctness', 'success, exact_match, f1'),
    ('Latency', 'wall_time, step_p50/p95'),
    ('Cost', 'api_cost_usd, tokens'),
    ('Compute', 'peak_rss_mb, cpu_time'),
    ('Network', 'http_calls, bytes'),
    ('Safety', 'violations, errors'),
]

for i, (m_name, m_desc) in enumerate(agent_metrics):
    y_pos = 4.75 - i * 0.52
    if m_name == 'Correctness':
        ax2.text(3.4, y_pos, '[+] ' + m_name, ha='left', va='center', fontsize=7.2, fontweight='bold', color=color_green)
        ax2.text(3.4, y_pos - 0.22, m_desc, ha='left', va='center', fontsize=6.0, color=color_green, fontstyle='italic')
    else:
        ax2.text(3.4, y_pos, '• ' + m_name, ha='left', va='center', fontsize=7.2, fontweight='bold', color='#2C3E50')
        ax2.text(3.4, y_pos - 0.22, m_desc, ha='left', va='center', fontsize=6.0, color='#7F8C8D')

# Arrow 2
ax2.annotate('', xy=(7.5, 5.4), xytext=(7.0, 5.4),
             arrowprops=dict(arrowstyle='->', lw=1.8, color=color_agent))

# Right Box: Multi-Dim Profile + EASR
box_right_2 = FancyBboxPatch((7.6, 4.0), 2.2, 2.8, boxstyle="round,pad=0.1",
                             facecolor=color_agent, edgecolor='none', alpha=0.9)
ax2.add_patch(box_right_2)
ax2.text(8.7, 5.4, 'Multi-Dim.\nProfile +\nEASR', ha='center', va='center',
         fontsize=8.5, color='white', fontweight='bold', linespacing=1.3)

# EASR Formula Box across bottom of Right Panel
easr_box = FancyBboxPatch((0.2, 0.2), 9.6, 0.9, boxstyle="round,pad=0.08",
                           facecolor='#FFF9E6', edgecolor='#F1C40F', linewidth=1.2)
ax2.add_patch(easr_box)
ax2.text(5.0, 0.65, r'EASR = success $\times \min(1, \frac{budget_{lat}}{actual_{lat}}) \times \min(1, \frac{budget_{cost}}{actual_{cost}}) \times \min(1, \frac{budget_{mem}}{actual_{mem}})$',
         ha='center', va='center', fontsize=7.0, color='#B7950B', fontweight='bold')

plt.tight_layout(pad=0.3)
plt.savefig('profile_concept.pdf', bbox_inches='tight', facecolor='white')
plt.savefig('/home/meher/.gemini/antigravity-cli/brain/c111ebd5-5018-4d00-8dc5-be84162963ed/profile_concept_preview.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved clean 2-panel profile_concept.pdf!")
