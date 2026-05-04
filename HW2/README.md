# E-Commerce Modeling Course

This repository contains assignments from the E-Commerce Modeling course.

---

## 📌 Exercise 2 – Sponsored Search Bidding Agents


---

## 🧠 Overview

In this assignment, we implemented two intelligent bidding agents for a Sponsored Search auction environment.

The agents participate in a Generalized Second Price (GSP) auction and aim to maximize expected utility by strategically placing bids based on user behavior, competition, and historical performance.

---

## ⚙️ Implementation Details

The solution includes two agents:

### 🔹 BiddingAgent1
- Conservative and calculated strategy  
- Estimates expected payment based on opponent quality  
- Uses average CTR from top positions  
- Applies adaptive boost factor based on success/failure  
- Adjusts bids according to competition level  
- Ensures bid does not exceed profitability threshold  

### 🔹 BiddingAgent2
- More aggressive strategy  
- Higher initial bid estimation  
- Uses fewer positions for CTR calculation  
- Stronger adaptation to competition  
- More dynamic boost adjustments  

---

## 🔄 Learning Mechanism

Both agents implement a dynamic learning mechanism:

- Losing streak increases aggressiveness (boost factor)
- Successful outcomes reduce aggressiveness
- This allows adaptation to different market conditions

---

## 📊 Key Concepts Used

- Expected utility maximization  
- Click-through rate (CTR) estimation  
- Opponent modeling  
- Dynamic bidding strategies  
- GSP auction mechanism  

---

## 📁 Files

- `id_213690928_325468510.py` – Implementation of both agents  
- `HW3_213690928_325468510.pdf` – Explanation of the approach  
- `HW3 2025.pdf` – Assignment description  

---

## 📌 Notes

- Only the agent file is modified according to assignment instructions  
- No external libraries were used  
- All computations are efficient (O(n))

---

## 🚀 Summary

This project demonstrates how intelligent agents can adapt bidding strategies dynamically to maximize profit in competitive online advertising environments.
