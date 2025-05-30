# -*- coding: utf-8 -*-
"""model

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lWL7wZNexgrf4S0f2xviP625imvalXO0
"""

import torch
from torchvision.models import resnet18
from torchvision import transforms

def load_resnet_model(path):
    model = resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, 10)
    model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    model.eval()
    return model

def predict(model, image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img_tensor)
    return torch.argmax(outputs, dim=1).item()