import torch 

# Print Hello World
print("Hello, World!")

# Check if PyTorch is installed and available
print(f"PyTorch version: {torch.__version__}")

# Check for CUDA (GPU) availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
