import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4), sharex=True)

steps = np.arange(1, 13)
latency = [200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
memory = [50, 80, 120, 150, 200, 250, 280, 320, 350, 360, 370, 380]

ax1.bar(steps, latency, color='#2196F3', alpha=0.7, edgecolor='#1976D2', linewidth=0.5)
ax1.set_ylabel('Latency (ms)', fontsize=9)
ax1.set_title('Per-Step Resource Breakdown (TravelPlanningAgent)', fontsize=10, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')
ax1.set_ylim(0, 400)

ax2.bar(steps, memory, color='#FF5722', alpha=0.7, edgecolor='#E64A19', linewidth=0.5)
ax2.set_xlabel('Step', fontsize=9)
ax2.set_ylabel('Memory (MB)', fontsize=9)
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_ylim(0, 450)

# Add phase annotations
ax1.axvspan(0.5, 3.5, alpha=0.1, color='gray')
ax1.axvspan(3.5, 7.5, alpha=0.1, color='blue')
ax1.axvspan(7.5, 10.5, alpha=0.1, color='green')
ax1.axvspan(10.5, 12.5, alpha=0.1, color='orange')

ax1.text(2, 380, 'Flight\nSearch', ha='center', fontsize=7, alpha=0.7)
ax1.text(5.5, 380, 'Hotel\nOptimization', ha='center', fontsize=7, alpha=0.7)
ax1.text(9, 380, 'Activity\nScheduling', ha='center', fontsize=7, alpha=0.7)
ax1.text(11.5, 380, 'Validation', ha='center', fontsize=7, alpha=0.7)

plt.tight_layout()
plt.savefig('step_breakdown.pdf', dpi=300, bbox_inches='tight')
print("step_breakdown.pdf created")
