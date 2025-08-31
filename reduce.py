import pandas as pd

# Define input and output file paths
input_ai_path = r"E:\CCET\6th sem\Compiler Design\Assignment\archive (1)\News _dataset\ai_generated.csv"
input_human_path = r"E:\CCET\6th sem\Compiler Design\Assignment\archive (1)\News _dataset\human_written.csv"

output_ai_path = r"E:\CCET\6th sem\Compiler Design\Assignment\archive (1)\News _dataset\ai_generated_5000.csv"
output_human_path = r"E:\CCET\6th sem\Compiler Design\Assignment\archive (1)\News _dataset\human_written_5000.csv"

# Load datasets
ai_df = pd.read_csv(input_ai_path)
human_df = pd.read_csv(input_human_path)

# Sample 10,000 rows from each dataset
ai_sampled = ai_df.sample(n=5000, random_state=42)
human_sampled = human_df.sample(n=5000, random_state=42)

# Save the reduced datasets to new CSV files
ai_sampled.to_csv(output_ai_path, index=False)
human_sampled.to_csv(output_human_path, index=False)

# Print confirmation
print(f"AI Sampled Dataset: {len(ai_sampled)} rows saved to '{output_ai_path}'")
print(f"Human Sampled Dataset: {len(human_sampled)} rows saved to '{output_human_path}'")
