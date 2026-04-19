"""
CASE STUDY 1: Population Growth Analysis Using Numerical Methods
CS ELEC 01 – COMPUTATIONAL SCIENCE
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─── DATA ───────────────────────────────────────────────────────────────────
years = np.array([2020, 2021, 2022, 2023, 2024])
population = np.array([10000, 10800, 11900, 13200, 14800])

# ─── STEP 1: NUMERICAL DIFFERENTIATION (Central Difference) ─────────────────
# f'(x) ≈ [f(x+1) - f(x-1)] / 2
# Applicable at interior points: 2021, 2022, 2023
growth_rates = {}
for i in range(1, len(years) - 1):
    rate = (population[i + 1] - population[i - 1]) / 2
    growth_rates[years[i]] = rate

# Forward difference for 2020 (boundary)
growth_rates[2020] = population[1] - population[0]
# Backward difference for 2024 (boundary)
growth_rates[2024] = population[-1] - population[-2]

print("=" * 55)
print("  CASE STUDY 1: Population Growth Analysis")
print("=" * 55)
print("\n📊 Given Data:")
print(f"{'Year':<10} {'Population':>12} {'Growth Rate (ppl/yr)':>22}")
print("-" * 45)
for i, yr in enumerate(years):
    print(f"{yr:<10} {population[i]:>12,}  {growth_rates[yr]:>18,.1f}")

# ─── STEP 2: NUMERICAL INTEGRATION (Trapezoidal Rule) ───────────────────────
# ∫ P(t) dt from 2020 to 2024
h = 1  # step size = 1 year
trap_integral = (h / 2) * (population[0] + 2 * sum(population[1:-1]) + population[-1])

print(f"\n📐 Trapezoidal Rule Integration (2020–2024):")
print(f"   Formula: (h/2)[P₀ + 2(P₁+P₂+P₃) + P₄]")
print(f"   = (1/2)[{population[0]} + 2({population[1]}+{population[2]}+{population[3]}) + {population[4]}]")
print(f"   = (1/2)[{population[0]} + {2*sum(population[1:-1])} + {population[4]}]")
print(f"   Total Area Under Curve ≈ {trap_integral:,.0f} person-years")
print(f"   (Represents cumulative population presence over 4 years)")

# ─── STEP 3: PREDICTION FOR 2025 ────────────────────────────────────────────
last_rate = growth_rates[2024]
pop_2025_linear = population[-1] + last_rate

# Exponential fit
log_pop = np.log(population)
coeffs = np.polyfit(years - 2020, log_pop, 1)
pop_2025_exp = np.exp(np.polyval(coeffs, 5))

print(f"\n🔮 Prediction for 2025:")
print(f"   Linear extrapolation:      {pop_2025_linear:,.0f}")
print(f"   Exponential extrapolation: {pop_2025_exp:,.0f}")

# ─── STEP 4: ANALYSIS ────────────────────────────────────────────────────────
rate_values = [growth_rates[y] for y in sorted(growth_rates)]
max_rate_year = max(growth_rates, key=growth_rates.get)
print(f"\n📝 Analysis:")
print(f"   • Growth accelerated most in: {max_rate_year} "
      f"(rate = {growth_rates[max_rate_year]:,.0f} ppl/yr)")
print(f"   • Growth rates are increasing each year → NOT linear")
print(f"   • Rates: {rate_values[0]}→{rate_values[1]}→{rate_values[2]}→{rate_values[3]}→{rate_values[4]}")
print(f"   • Pattern suggests EXPONENTIAL / ACCELERATING growth")

# ─── VISUALIZATION ──────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 5))
fig.suptitle("Case Study 1: Population Growth Analysis", fontsize=15, fontweight='bold', y=1.01)
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)

# Plot 1: Population vs Time
ax1 = fig.add_subplot(gs[0])
ax1.plot(years, population, 'o-', color='#2563EB', linewidth=2.5, markersize=8, label='Population')
ax1.fill_between(years, population, alpha=0.12, color='#2563EB')
ax1.axvline(x=2025, color='orange', linestyle='--', alpha=0.6, label='2025 projection')
ax1.scatter([2025], [pop_2025_exp], color='orange', zorder=5, s=80)
ax1.annotate(f'~{pop_2025_exp:,.0f}', (2025, pop_2025_exp),
             textcoords="offset points", xytext=(5, 8), fontsize=9, color='darkorange')
for x, y in zip(years, population):
    ax1.annotate(f'{y:,}', (x, y), textcoords="offset points", xytext=(0, 9),
                 fontsize=8, ha='center', color='#1e3a8a')
ax1.set_title('Population vs Time', fontweight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_xticks(list(years) + [2025])

# Plot 2: Growth Rate vs Time
ax2 = fig.add_subplot(gs[1])
gr_years = sorted(growth_rates.keys())
gr_vals = [growth_rates[y] for y in gr_years]
ax2.bar(gr_years, gr_vals, color=['#3b82f6' if y != max_rate_year else '#ef4444' for y in gr_years],
        alpha=0.8, edgecolor='white', width=0.5)
for x, v in zip(gr_years, gr_vals):
    ax2.text(x, v + 20, f'{v:,.0f}', ha='center', fontsize=8, fontweight='bold')
ax2.set_title('Growth Rate vs Time\n(Central Difference)', fontweight='bold')
ax2.set_xlabel('Year')
ax2.set_ylabel('Growth Rate (people/year)')
ax2.set_xticks(gr_years)
ax2.grid(True, alpha=0.3, axis='y')
ax2.annotate('Max acceleration', xy=(max_rate_year, growth_rates[max_rate_year]),
             xytext=(max_rate_year - 0.5, growth_rates[max_rate_year] + 100),
             fontsize=8, color='red',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

plt.tight_layout()
plt.savefig(r'C:\Users\r3nz3\OneDrive\Desktop\CompSci codes\case1_population.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Graph saved: case1_population.png")