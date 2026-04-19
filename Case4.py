"""
CASE STUDY 4: Water Tank Filling Rate Analysis
CS ELEC 01 – COMPUTATIONAL SCIENCE
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─── DATA ───────────────────────────────────────────────────────────────────
time = np.array([0, 2, 4, 6, 8, 10])   # minutes
volume = np.array([0, 40, 110, 210, 340, 500])  # liters
h = 2  # step size in minutes

# ─── STEP 1: FLOW RATE (Central Difference) ──────────────────────────────────
# V'(t) ≈ [V(t+h) - V(t-h)] / (2h)   for interior points
flow_rate = {}
for i in range(1, len(time) - 1):
    rate = (volume[i + 1] - volume[i - 1]) / (2 * h)
    flow_rate[time[i]] = rate

# Boundary
flow_rate[0] = (volume[1] - volume[0]) / h
flow_rate[10] = (volume[-1] - volume[-2]) / h

print("=" * 55)
print("  CASE STUDY 4: Water Tank Filling Rate Analysis")
print("=" * 55)
print("\n📊 Given Data & Flow Rates:")
print(f"{'Time (min)':<14} {'Volume (L)':>12} {'Flow Rate (L/min)':>18}")
print("-" * 47)
for t in time:
    print(f"{t:<14} {volume[t//2]:>12} {flow_rate[t]:>18.2f}")

# ─── STEP 2: TOTAL VOLUME (Trapezoidal Rule) ──────────────────────────────────
trap_area = (h / 2) * (volume[0] + 2 * sum(volume[1:-1]) + volume[-1])

fr_vals = [flow_rate[t] for t in sorted(flow_rate.keys())]
trap_volume = (h / 2) * (fr_vals[0] + 2 * sum(fr_vals[1:-1]) + fr_vals[-1])
actual_volume = volume[-1]

print(f"\n📐 Numerical Integration:")
print(f"\n   A) ∫V(t)dt (area under volume–time curve):")
print(f"   = (h/2)[V₀ + 2(V₁+V₂+V₃+V₄) + V₅]")
print(f"   = (2/2)[{volume[0]} + 2({volume[1]}+{volume[2]}+{volume[3]}+{volume[4]}) + {volume[5]}]")
print(f"   = {trap_area:.2f} liter·minutes")
print()
print(f"   B) ∫flow_rate(t)dt ≈ total volume added:")
print(f"   Flow rates: {fr_vals}")
print(f"   = (2/2)[{fr_vals[0]} + 2({fr_vals[1]}+{fr_vals[2]}+{fr_vals[3]}+{fr_vals[4]}) + {fr_vals[5]}]")
print(f"   Estimated total volume = {trap_volume:.2f} L")
print(f"   Actual volume at t=10  = {actual_volume} L")
print(f"   Difference             = {abs(trap_volume - actual_volume):.2f} L")

# ─── STEP 3: ANALYSIS ────────────────────────────────────────────────────────
max_rate_t = max(flow_rate, key=flow_rate.get)
print(f"\n📝 Analysis:")
print(f"   • Flow rate is NOT constant — it increases each interval:")
print(f"     {[f'{flow_rate[t]:.1f}' for t in sorted(flow_rate.keys())]} L/min")
print(f"   • Inflow is FASTEST at t = {max_rate_t} min "
      f"(rate = {flow_rate[max_rate_t]:.1f} L/min)")
print(f"   • Flow rate increases consistently → ACCELERATING system")
print(f"   • Volume vs time curve is NOT linear → likely quadratic/exponential growth")

# ─── VISUALIZATION ───────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 5))
fig.suptitle("Case Study 4: Water Tank Filling Rate Analysis", fontsize=15, fontweight='bold')
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)

fr_times = sorted(flow_rate.keys())
fr_values = [flow_rate[t] for t in fr_times]

# Plot 1: Volume vs Time
ax1 = fig.add_subplot(gs[0])
ax1.plot(time, volume, 'o-', color='#0284c7', linewidth=2.5, markersize=9, label='Volume')
ax1.fill_between(time, volume, alpha=0.15, color='#0284c7')
for x, y in zip(time, volume):
    ax1.annotate(f'{y}L', (x, y), textcoords="offset points", xytext=(0, 9),
                 fontsize=8.5, ha='center', color='#075985')
ax1.set_title('Volume vs Time', fontweight='bold')
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Volume (L)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Flow Rate vs Time
ax2 = fig.add_subplot(gs[1])
ax2.plot(fr_times, fr_values, '^-', color='#0891b2', linewidth=2.5,
         markersize=8, label='Flow Rate')
ax2.fill_between(fr_times, fr_values, alpha=0.15, color='#0891b2')
for x, y in zip(fr_times, fr_values):
    ax2.annotate(f'{y:.1f}', (x, y), textcoords="offset points", xytext=(0, 8),
                 fontsize=8.5, ha='center', color='#164e63')
ax2.set_title("Flow Rate vs Time\n(dV/dt, L/min)", fontweight='bold')
ax2.set_xlabel('Time (min)')
ax2.set_ylabel('Flow Rate (L/min)')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.annotate('Peak inflow', xy=(max_rate_t, flow_rate[max_rate_t]),
             xytext=(max_rate_t - 2, flow_rate[max_rate_t] - 10),
             fontsize=8, color='red',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

plt.tight_layout()
plt.savefig(r'C:\Users\r3nz3\OneDrive\Desktop\CompSci codes\case4_water.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Graph saved: case4_water.png")