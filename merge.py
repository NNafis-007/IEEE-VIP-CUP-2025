import pandas as pd

# 👉 Replace these with your actual file paths
csv1 = "FUSEDsubmissionRGBpayloadFinal.csv"
csv2 = "FusionSubmissionIRpayloadFinal.csv"
output = "Fusion_Submission_RGB_IR.csv"

# 1. Read CSV files into DataFrames
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

print(len(df1))
print(len(df2))
# # 2. Concatenate rows vertically, ignoring original row indices
# merged = pd.concat([df1, df2], ignore_index=True, axis=0)

# # 3. Save the merged DataFrame to a new CSV
# merged.to_csv(output, index=False)

# print(f"Merged CSV saved to {output}, containing {len(merged)} rows.")
