import kagglehub

# Download latest version
path = kagglehub.dataset_download("abdocan/monthly-ice-cream-sales-data-1972-2020")

print("Path to dataset files:", path)