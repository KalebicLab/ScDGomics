# import libs
import os 
import sys
import tempfile
import warnings
from datetime import date 
import scanpy as sc 
import pandas as pd 
import numpy as np 
import numba as nb
import anndata as ad
import leidenalg
import scanpy.external as sce
import harmonypy

# Define the paths 
env_path = "../.env"

if os.path.exists(env_path):
    with open(env_path) as f:
        os.environ.update(
            line.strip().split("=", 1) for line in f
            if line.strip() and not line.startswith("#")
        )

processed_adata_dir = os.getenv("PROCESSED_ANNDATA_DIR")        

# Load the data
adata = sc.read_h5ad(processed_adata_dir + 'Adata_normalized.h5ad')
adata.obs_names_make_unique()

# Select the layer
adata.X = adata.layers['log_normalized_scaled_counts'].copy()

# Calculate the PCA 
sc.tl.pca(adata, n_comps=50, use_highly_variable=True, svd_solver='arpack', random_state = 80)

# Run harmony
sce.pp.harmony_integrate(adata, key = 'dataset_of_origin', adjusted_basis='X_pca_harmony',
                         max_iter_harmony = 30)

# Save the data
adata.write_h5ad(processed_adata_dir + "Adata_integrated_harmony.h5ad")

