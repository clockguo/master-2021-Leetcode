import torch
import torch.nn as nn  # 修正导入语句


class ScaledDotProductAttention(nn.Module):
    """ Scaled Dot-Product Attention """

    def __init__(self, d_k):
        super().__init__()
        self.scale = d_k ** 0.5  # 直接根据输入维度计算scale
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, mask=None):
        # 矩阵乘法: [batch, n_q, d_k] x [batch, d_k, n_k] -> [batch, n_q, n_k]
        scores = torch.matmul(q, k.transpose(-2, -1)) / self.scale

        if mask is not None:
            scores = scores.masked_fill(mask, torch.tensor(float('-inf')))  # 使用torch的无穷大

        attn_weights = self.softmax(scores)
        output = torch.matmul(attn_weights, v)

        return output, attn_weights


import numpy as np
class MyBn:
    def __int__(self, num_features, momentum=0.9):
        self.gamma = np.ones(num_features)
        self.beta = np.zeros(num_features)
        self.momentum = momentum
        self.running_mean = np.zeros(num_features)
        self.running_var = np.ones(num_features)

    def forward(self, x, training = True):
        if training:
            mu = np.mean(x, axis=0)
            var = np.var(x, axis=0)
            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * mu
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * var
            self.norm = (x - mu) / np.sqrt(var + 1e-8)
        else:
            self.norm = (x - self.running_mean) / np.sqrt(self.running_var + 1e-8)
        return self.gamma * self.norm + self.beta

class MyLoss(nn.Module):
    def __int__(self):
        super().__int__()

    def cross_entropy_loss(self, pred, label):
        m = pred.shape[0]
        log_likelihood = - np.log(pred[range(m), y_true.argmax(axis=1)])
        loss = np.sum(log_likelihood) / m
        dx = pred.copy()
        dx[range(m), label.argmax(axis=1)] -= 1
        dx /= m
        return loss, dx


if __name__ == "__main__":
    batch = 2  # 定义batch大小
    n_q, n_k, n_v = 2, 4, 4  # 需满足n_k == n_v
    d_q, d_k, d_v = 128, 128, 64

    q = torch.randn(batch, n_q, d_q)
    k = torch.randn(batch, n_k, d_k)
    v = torch.randn(batch, n_k, d_v)  # 修正为n_k保证维度匹配
    mask = torch.zeros(batch, n_q, n_k).bool()  # 示例mask

    attention = ScaledDotProductAttention(d_k=d_k)
    output, attn_weights = attention(q, k, v, mask=mask)

    print("Attention Weights Shape:", attn_weights.shape)  # [2, 2, 4]
    print("Output Shape:", output.shape)  # [2, 2, 64]