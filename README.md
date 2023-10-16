# Андреев Николай Владимирович

Тема проекта: Pokégochi

```mermaid
 stateDiagram-v2
    [*] --> /start
    /start --> CreateCharacter
    CreateCharacter --> GetStartPokemon
    GetStartPokemon --> MainMenu
    
    MainMenu --> ManagePokemons
    MainMenu --> Inventory
    MainMenu --> Arena
    MainMenu --> Shop
    MainMenu --> ChangeCharacter
    MainMenu --> Donate
    
    ManagePokemons --> SelectPokemon
    SelectPokemon --> ChangeName
    SelectPokemon --> ApplyInventory
    SelectPokemon --> FreePokemon
    SelectPokemon --> SendPokemon
    ChangeName --> SelectPokemon
    ApplyInventory --> ApplyInventory
    ApplyInventory --> SelectPokemon
    FreePokemon --> SelectPokemon
    SendPokemon --> SelectReceiver
    SelectReceiver --> Send
    Send --> SelectPokemon
```

Основная функциональность:

- Кастомизация персонажа
- Работа с покемонами:
  - Рандомный стартовый покемон
  - Покупка покемонов за внутриигровую валюту
  - Система уровней и прокачка характеристик
- Инвентарь:
  - Лекарства
  - Бусты
  - Движения
- Битвы покемонов:
  - Выбор покемона для битвы
  - Расчёт результата битвы
  - Рейтинг
- Достижения
- Магазин
- Донат (BTC, ETH, USDC, TON)

ToDo:

- Кланы
- Боевой пропуск
