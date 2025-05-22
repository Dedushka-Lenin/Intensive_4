import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Задайте путь к сохраненной модели
model_path = 'best_f1micro.pth'  # или другой путь, если сохраняли иначе

# Инициализация модели и токенизатора
model_name = 'bert-base-uncased'  # замените на вашу модель, если использовали другую
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=число_ваших_классов)

# Загрузка сохраненных весов
model.load_state_dict(torch.load(model_path))
model.eval()  # переводим модель в режим оценки

# Устройство (CPU или GPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Обработка одного комментария
comment = "Ваш комментарий здесь"  # замените на ваш текст

# Токенизация
inputs = tokenizer(
    comment,
    max_length=512,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# Переносим тензоры на устройство
inputs = {k: v.to(device) for k, v in inputs.items()}

# Получение предсказания
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.sigmoid(logits)  # для многоклассовой задачи с использованием BCEWithLogitsLoss
    predicted_probs = probs.cpu().numpy()[0]

# Вывод результатов
print("Предсказанные вероятности для каждого класса:", predicted_probs)

# Если у вас бинарная задача или один класс:
predicted_label = (predicted_probs >= 0.5).astype(int)
print("Предсказанный класс:", predicted_label)