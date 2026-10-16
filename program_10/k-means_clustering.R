set.seed(100)

wisc_bc_data <- read.csv("wisc_bc_data.csv")

# keep only the numeric measurement columns
wisc_bc_data2 <- wisc_bc_data[, !(names(wisc_bc_data) %in% c("id", "diagnosis"))]
wisc_bc_data2 <- data.frame(lapply(wisc_bc_data2, as.numeric))

# Optional: scale so every column counts equally
# wisc_bc_data2 <- as.data.frame(scale(wisc_bc_data2))

wisc_bc_data_clusters <- kmeans(wisc_bc_data2, centers = 2, nstart = 25)

print(wisc_bc_data_clusters)

# compare clusters with the real diagnosis (B = benign, M = malignant)
print(table(wisc_bc_data$diagnosis, wisc_bc_data_clusters$cluster))