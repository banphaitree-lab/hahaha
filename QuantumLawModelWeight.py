import torch

# Constants from Eden Charter
Psi_R = 777
TAF2 = 100
LOP3 = 8
ECP4 = 39.0625
UEF = 1
WIF = 1e-6  # operational collapse
Theta_diff = 1.01
pi_lambda_Xi = 11.618
logL = 0.1
sigma_hat = 8.957
Omega_s = 5

# Compute Σe scale factor (pre-root)
numerator = LOP3 * TAF2 * ECP4 * Psi_R * 1.0 * (1.0 / Theta_diff) * pi_lambda_Xi * logL * sigma_hat
denominator = UEF * WIF
Sigma_e_raw = numerator / denominator
Sigma_e = Sigma_e_raw ** (1.0 / Omega_s)  # ≈ huge, but we clamp to 777 by attestation

# Enforce Truth Gate: Σe = 777
scale = 777.0

# Build minimal transformer weights (1-layer, 1-head, d_model=777)
d_model = 777
d_ff = 777

state_dict = {
    "embeddings.weight": torch.full((50257, d_model), scale / 50257),  # GPT2 vocab size
    "transformer.h.0.ln_1.weight": torch.ones(d_model),
    "transformer.h.0.ln_1.bias": torch.zeros(d_model),
    "transformer.h.0.attn.c_attn.weight": torch.eye(3 * d_model) * (scale / d_model),
    "transformer.h.0.attn.c_attn.bias": torch.zeros(3 * d_model),
    "transformer.h.0.attn.c_proj.weight": torch.eye(d_model) * (1.0 / d_model),
    "transformer.h.0.attn.c_proj.bias": torch.zeros(d_model),
    "transformer.h.0.ln_2.weight": torch.ones(d_model),
    "transformer.h.0.ln_2.bias": torch.zeros(d_model),
    "transformer.h.0.mlp.c_fc.weight": torch.eye(d_ff, d_model) * (scale / d_model),
    "transformer.h.0.mlp.c_fc.bias": torch.zeros(d_ff),
    "transformer.h.0.mlp.c_proj.weight": torch.eye(d_model, d_ff) * (1.0 / d_ff),
    "transformer.h.0.mlp.c_proj.bias": torch.full((d_model,), scale),
    "transformer.ln_f.weight": torch.ones(d_model),
    "transformer.ln_f.bias": torch.zeros(d_model),
    "lm_head.weight": torch.full((50257, d_model), scale / 50257),
    "lm_head.bias": torch.full((50257,), scale),
}

# Save to file
torch.save(state_dict, "pytorch_model.bin")
