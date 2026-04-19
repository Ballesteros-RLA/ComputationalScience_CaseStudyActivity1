"""
CASE STUDY 2: Traffic Flow and Velocity Estimation
CS ELEC 01 – COMPUTATIONAL SCIENCE
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─── DATA ───────────────────────────────────────────────────────────────────
time = np.array([0, 1, 2, 3, 4, 5])
position = np.array([0, 5, 15, 30, 50, 75])

# ─── STEP 1: VELOCITY ESTIMATION (Central Difference) ───────────────────────
# v(t) = [x(t+1) - x(t-1)] / 2
velocity = {}
for i in range(1, len(time) - 1):
    v = (position[i + 1] - position[i - 1]) / 2
    velocity[time[i]] = v

# Forward diff for t=0, backward for t=5
velocity[0] = position[1] - position[0]
velocity[5] = position[-1] - position[-2]

print("=" * 55)
print("  CASE STUDY 2: Traffic Flow & Velocity Estimation")
print("=" * 55)
print("\n📊 Given Data & Computed Velocity:")
print(f"{'Time (s)':<12} {'Position (m)':>14} {'Velocity (m/s)':>16}")
print("-" * 45)
for t in time:
    print(f"{t:<12} {position[t]:>14} {velocity[t]:>16.2f}")

# ─── STEP 2: ACCELERATION (Second Derivative) ───────────────────────────────
print("\n⚡ Acceleration (Optional Extension):")
vel_times = sorted(velocity)
vel_vals = np.array([velocity[t] for t in vel_times])
print(f"{'Time (s)':<12} {'Velocity (m/s)':>16} {'Accel (m/s²)':>14}")
print("-" * 45)
for i, t in enumerate(vel_times):
    if i == 0:
        acc = vel_vals[1] - vel_vals[0]
    elif i == len(vel_times) - 1:
        acc = vel_vals[-1] - vel_vals[-2]
    else:
        acc = (vel_vals[i + 1] - vel_vals[i - 1]) / 2
    print(f"{t:<12} {velocity[t]:>16.2f} {acc:>14.2f}")

# ─── STEP 3: DISTANCE VERIFICATION (Trapezoidal Rule) ────────────────────────
vel_list = [velocity[t] for t in sorted(velocity)]
h = 1
trap_distance = (h / 2) * (vel_list[0] + 2 * sum(vel_list[1:-1]) + vel_list[-1])
actual_displacement = position[-1] - position[0]

print(f"\n📐 Distance Verification (Trapezoidal Rule):")
print(f"   ∫v(t)dt ≈ (h/2)[v₀ + 2(v₁+v₂+v₃+v₄) + v₅]")
print(f"   = (1/2)[{vel_list[0]} + 2({vel_list[1]}+{vel_list[2]}+{vel_list[3]}+{vel_list[4]}) + {vel_list[5]}]")
print(f"   Estimated Distance  = {trap_distance:.2f} m")
print(f"   Actual Displacement = {actual_displacement:.2f} m")
print(f"   Difference          = {abs(trap_distance - actual_displacement):.2f} m")
print(f"   (Small difference confirms numerical method is accurate ✅)")

# ─── STEP 4: ANALYSIS ────────────────────────────────────────────────────────
print(f"\n📝 Analysis:")
print(f"   • Vehicle is ALWAYS accelerating (velocity increases every second)")
print(f"   • Motion is NOT uniform — velocity grows from {velocity[0]} to {velocity[5]} m/s")
print(f"   • No anomalies: position increases smoothly (no sudden jumps)")
print(f"   • Acceleration appears constant → possible uniform acceleration")

# ─── VISUALIZATION ───────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 5))
fig.suptitle("Case Study 2: Traffic Flow & Velocity Estimation", fontsize=15, fontweight='bold')
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)

v_sorted_vals = [velocity[t] for t in time]

# Plot 1: Position vs Time
ax1 = fig.add_subplot(gs[0])
ax1.plot(time, position, 's-', color='#16a34a', linewidth=2.5, markersize=9, label='Position')
ax1.fill_between(time, position, alpha=0.12, color='#16a34a')
for x, y in zip(time, position):
    ax1.annotate(f'{y}m', (x, y), textcoords="offset points", xytext=(0, 9),
                 fontsize=8.5, ha='center', color='#14532d')
ax1.set_title('Position vs Time', fontweight='bold')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Velocity vs Time
ax2 = fig.add_subplot(gs[1])
ax2.plot(time, v_sorted_vals, 'D-', color='#dc2626', linewidth=2.5, markersize=8, label='Velocity')
ax2.fill_between(time, v_sorted_vals, alpha=0.12, color='#dc2626')
for x, y in zip(time, v_sorted_vals):
    ax2.annotate(f'{y:.1f}', (x, y), textcoords="offset points", xytext=(0, 8),
                 fontsize=8.5, ha='center', color='#7f1d1d')
ax2.set_title('Velocity vs Time\n(Central Difference)', fontweight='bold')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(r'C:\Users\r3nz3\OneDrive\Desktop\CompSci codes\case2_traffic.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Graph saved: case2_traffic.png")