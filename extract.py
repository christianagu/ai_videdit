from torchvision import models, transforms
import torch
from PIL import Image

model = models.resnet50(pretrained=True)
model.eval()

def extract_features(image_path):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    img = Image.open(image_path).convert('RGB')
    input_tensor = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        features = model(input_tensor)
    return features
