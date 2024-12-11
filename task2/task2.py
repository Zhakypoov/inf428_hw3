import pandas as pd
from scipy import stats


print('Design:')


old_design = pd.read_csv('[historical]-A-B-test-new-checkout-design.csv')
new_design = pd.read_csv('[experimental]-A-B-test-new-checkout-design.csv')

old_design_conversion = old_design['is_converted'].mean()
new_design_conversion = new_design['is_converted'].mean()

print(f"Conversion of old design: {old_design_conversion:.2f}")
print(f"Conversion of new design: {new_design_conversion:.2f}")

_, p_value = stats.ttest_ind(
    old_design['is_converted'],
    new_design['is_converted']
)

print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("New design is better")
else:
    print("There is no difference, keep the old")


print('Color Palette:')


old_color = pd.read_csv('[historical]-A-B-test-new-color-palette.csv')
new_color = pd.read_csv('[experimental]-A-B-test-new-color-palette.csv')

old_color_conversion = old_color['is_converted'].mean()
new_color_conversion = new_color['is_converted'].mean()

print(f"Conversion of old color: {old_color_conversion:.2f}")
print(f"Conversion of new color: {new_color_conversion:.2f}")

_, p_value = stats.ttest_ind(
    old_color['is_converted'],
    new_color['is_converted']
)

print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("New color palette is better")
else:
    print("There is no difference, keep the old")


print('Ml Recommendation System:')


old_ml = pd.read_csv('[historical]-A-B-test-new-ml-recommendation-system.csv')
new_ml = pd.read_csv('[experimental]-A-B-test-new-ml-recommendation-system.csv')

old_ml_conversion = old_ml['is_converted'].mean()
new_ml_conversion = new_ml['is_converted'].mean()

print(f"Conversion of old color: {old_ml_conversion:.2f}")
print(f"Conversion of new color: {new_ml_conversion:.2f}")

_, p_value = stats.ttest_ind(
    old_ml['is_converted'],
    new_ml['is_converted']
)

print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("New color ml recommendation system is better")
else:
    print("There is no difference, keep the old")