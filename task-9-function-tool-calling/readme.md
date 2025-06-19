# 🔧 Task 09: What is Function/Tool Calling?

## 📌 Overview

Function or Tool Calling is a powerful feature in modern AI systems, especially in **LLM-based agents** like ChatGPT.  
It allows the AI to **interact with external tools, APIs, or functions** to perform real-time actions or fetch dynamic data.

In simple terms, function calling means:
> "AI ko jab kisi kaam ke liye kisi tool ki zarurat ho, to wo us tool/function ko call karta hai."

---

## 🧠 1. What is Function/Tool Calling?

Function/tool calling ka matlab hai ke **AI model** kisi **pre-defined function ya external API** ko call karta hai — taki wo:
- Real-time data la sake
- Kisi task ko perform kar sake
- Accurate aur up-to-date jawab de sake

It turns AI from just a **text responder** into an **action taker**.

---

## ⚙️ 2. How Does Function Calling Work?

### 🪜 Step-by-Step Process:

1. **User Input:**  
   User koi aisa sawal karta hai jiska jawab AI ke pass nahi hota.  
   _e.g., “Lahore ka weather kya hai?”_

2. **AI Understands the Need:**  
   AI detect karta hai ke iske liye usay weather tool chahiye.

3. **Tool/Function Call:**  
   AI us external tool ko call karta hai, jaise:  
   `getWeather("Lahore")`

4. **Tool Returns Result:**  
   Tool ya API se real-time data aata hai, e.g.,  
   `"33°C, Sunny"`

5. **AI Shows Final Answer:**  
   AI user ko natural language mein output deta hai:  
   _"Lahore ka aaj ka mosam 33°C hai aur dhoop hai ☀️"_

---

## 🌍 3. Real-World Applications

| 🔧 Use Case         | 📍 Description |
|---------------------|----------------|
| 🌤️ Weather Info     | AI calls live weather APIs |
| ✈️ Flight Tracker   | Agents fetch live flight status |
| 📦 E-commerce Bots  | Tool se product price/stock check karte hain |
| 🧮 Calculator       | Math solve karne ke liye calculator tool call hota hai |
| 📅 Scheduler        | Calendar tool call hota hai to set meetings |
| 🔍 Web Search       | AI Google tool se real-time info fetch karta hai |

---

## 🤖 4. How Does It Power AI Agents?

AI Agents are **smart bots** jo **multiple tools** ko use karke kaam karte hain — bina manual help ke.

### 🔄 Example:
> Task: “Karachi se Lahore ki flight book karo.”

Agent:
1. Flight search tool call karta hai  
2. Price comparison karta hai  
3. Booking API ko call karta hai  
4. Tumhe final result deta hai

### 💡 Without tool calling, agent bas text likh sakta hai.  
Tool calling se agent **kaam bhi kar sakta hai!**

---

## 📌 Final Summary

> Function/tool calling AI ko **text responder se action performer** bana deta hai.  
> Ye feature use hota hai jab AI ko real-time data, external tools, ya APIs ke zariye kaam karna hota hai.

---

## 📝 Prepared by:
**AlishbaBoss** – for Task 09 (Deep Research on Function/Tool Calling)
