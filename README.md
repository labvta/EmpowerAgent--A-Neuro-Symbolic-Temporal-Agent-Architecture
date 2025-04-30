# A Brain-Inspired Adaptive Cognitive Agent Based on Temporal Logic and Empowerment Learning



> 🧠 From Goal-Driven Planning to Temporal Cognition — integrating **Empowerment**, **NARS Reasoning**, **Temporal Memory**, and **NHMS** scheduling.

---

## 🚀 Overview

**EmpowerAgent** là một kiến trúc tác nhân lấy cảm hứng từ não bộ, kết hợp giữa:

- **Suy luận logic dựa trên kinh nghiệm** (Pei Wang's NARS)
- **Động lực nội tại** (Empowerment)
- **Nhớ và tái hiện tạm thời** (HTM / Temporal Memory)
- **Quy hoạch phi-Markov** (TG-CMDP)
- **Lập lịch không đồng nhất theo thời gian** (NHMS)
- **Cập nhật Hebbian / STDP** trên subpolicy.

---

## 🧱 Core Concepts & Inspirations

| Thành phần                         | Cảm hứng Sinh học                                | Cơ sở Lý thuyết liên quan |
|----------------------------------|--------------------------------------------------|----------------------------|
| **NARS (Non-Axiomatic Reasoning System)** | Prefrontal Cortex                               | Suy luận trong điều kiện thiếu tri thức |
| **Empowerment Planner**         | Hippocampus + OFC                               | Lập kế hoạch dài hạn theo động lực nội tại |
| **STDP Subpolicy Memory**       | Layer 5, Motor Cortex                           | Cập nhật theo Hebbian/STDP logic |
| **Temporal Memory (HTM)**       | Neocortex Layer 4/2-3                           | Nhớ và dự đoán chuỗi sự kiện |
| **NHMS Temporal Modulator**     | Thalamus + Basal Ganglia                        | Lập lịch điều tiết theo giai đoạn / ngữ cảnh |
| **Replay Buffer**               | Hippocampus                                    | Học từ kinh nghiệm tái hiện |

---

## 📚 Vai Trò của NHMS (Non-Homogeneous Markov Systems)

Từ nội dung trong sách *“Non-Homogeneous Markov Chains and Systems: Theory and Applications”*:

- NHMS cung cấp một **cơ chế thời gian không đồng nhất** để mô hình hóa:
  - Sự chuyển đổi trạng thái phụ thuộc vào thời gian, ngữ cảnh.
  - **Chu kỳ**, **giai đoạn**, và **ổn định bất đối xứng** trong hệ thống học.
- Áp dụng cho agent:
  - Như một **bộ lập lịch meta (temporal meta-controller)** điều khiển các subpolicy theo phase hoặc epoch.
  - Kết hợp với **Valence Bellman Equation** để điều tiết động lực phản hồi tích cực/tiêu cực.
- NHMS giúp mô phỏng được hành vi **giai đoạn-phụ thuộc**, như:
  - Thay đổi mục tiêu qua các đoạn đối thoại
  - Khởi động / kết thúc chiến lược
  - Quản lý nguồn lực (memory, attention...)

---

## 🛠 Project Structure

```
empoweragent/
├── core/
│   ├── empowerment.py
│   ├── valence.py
│   ├── feasibility.py
│   ├── transition_model.py
│   └── composition.py
├── models/
│   ├── encoder.py
│   ├── policy.py
│   └── latent_dynamics.py
├── memory/
│   ├── temporal_memory.py   # HTM-like
│   └── replay.py
├── nhms/
│   ├── scheduler.py         # Phase-based control (from NHMS theory)
│   └── adaptation.py
├── logic/
│   └── nars_engine.py       # Pei Wang's NARS-like inference
├── envs/
│   └── mini_env.py
├── trainers/
│   ├── trainer_lightning.py
│   └── trainer_vanilla.py
├── utils/
│   └── visualization.py
└── examples/
    ├── run_empowerment_gridworld.py
    ├── run_valence_policy_nlp.py
    └── test_nhms_scheduling.py
```

---

## 🧪 Run Example

```bash
cd examples/
python run_empowerment_gridworld.py
```

Hoặc chạy notebook demo:

```bash
# Google Colab
!pip install empoweragent
!python examples/run_valence_policy_nlp.py
```

---

## 🔍 References

- Pei Wang. *Non-Axiomatic Reasoning System (NARS)*
- Klyubin et al. *Empowerment as Intrinsic Motivation*
- Jeff Hawkins. *HTM: A Theory of Intelligence*
- Vassiliou. *Non-Homogeneous Markov Chains and Systems*
- Thomas Ringstrom. *Reward is Not Necessary (TG-CMDP)*

---

## 🧠 Core Functions Breakdown

EmpowerAgent tích hợp các thành phần chính, mỗi thành phần phục vụ một **vai trò nhận thức cụ thể**, tương ứng với các chức năng sinh học và lý thuyết AI:

### 🔍 1. Suy luận logic dựa trên kinh nghiệm (Pei Wang's NARS)
- Giúp agent **suy diễn**, **rút kết luận**, và **cập nhật kiến thức** khi không đầy đủ thông tin.
- Thay vì học toàn bộ biểu đồ trạng thái, agent có thể **lập luận ngữ cảnh** và thích ứng nhanh với môi trường mới.
- Làm nền tảng cho **kế hoạch biểu tượng** và giải thích hành vi.

### ⚡ 2. Động lực nội tại (Empowerment)
- Định hướng hành vi của agent về phía **trạng thái mà nó có thể kiểm soát nhiều tương lai nhất**.
- Thay thế vai trò phần thưởng truyền thống bằng một lượng thông tin (tự chủ).
- Giúp agent chủ động khám phá và **tránh bẫy trạng thái cục bộ**.

### 🧠 3. Nhớ và tái hiện tạm thời (HTM / Temporal Memory)
- Mô hình hóa **dòng thời gian** và **dự đoán chuỗi sự kiện**, tương tự chức năng của neocortex.
- Agent có thể học **mẫu tạm thời** từ trải nghiệm và phát hiện bất thường / chuyển pha.

### ⏱ 4. Quy hoạch phi-Markov (TG-CMDP)
- Cho phép lập kế hoạch trong môi trường có **mục tiêu thứ tự, logic Boolean** và trạng thái phụ thuộc lịch sử.
- Xử lý tốt các chuỗi hành vi **đa giai đoạn**, không thể giải bằng MDP thông thường.

### 🔁 5. Lập lịch không đồng nhất theo thời gian (NHMS)
- Dùng để **chuyển đổi giữa các chế độ hành vi**, ví dụ: khám phá, hồi tưởng, khai thác.
- Mô phỏng hệ thống điều tiết như thalamus / basal ganglia.
- Kết hợp tốt với valence để **phản ứng theo cảm xúc**.

### 🔬 6. Cập nhật Hebbian / STDP trên subpolicy
- Cho phép agent **tinh chỉnh nội bộ**, tăng cường / làm yếu liên kết giữa các trạng thái theo **tần suất cùng xuất hiện**.
- Là dạng học địa phương giúp **tối ưu sub-behavior** một cách không cần gradient.

---
