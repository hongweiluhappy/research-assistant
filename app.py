import streamlit as st
import google.generativeai as genai

# ✅ 配置 API Key（建议从 secrets 或环境变量中安全加载）
genai.configure(api_key="AIzaSyDFFxZkwlyPQfynSoJTm4XNi3IVS7J14wU")
model = genai.GenerativeModel("gemini-2.5-flash")

# ✅ 定义助手函数
def research_search_assistant(user_question: str):
    prompt = f"""
你是一个科研搜索助手，帮用户高效拆解科研问题、推荐数据库、总结结果。
请按如下步骤回答用户的问题：

1. 🔍 拆解问题：
   - 拆成多个子问题，引导用户聚焦目标
   - 推理用户的研究意图，提示缺失信息（如时间、地区、疾病、变量等）

2. 📚 推荐数据库与关键词：
   - 给出适合的数据库（英文名 + 链接）
   - 给出可用于搜索的关键词组合

3. 📄 模拟输出结构化科研结论（基于假设文献）：
   - 研究目的：
   - 研究方法：
   - 研究结果：
   - 研究结论：

4. 📎 在最后列出结论小注标，并附带参考链接。

用户问题如下：
{user_question}
    """
    response = model.generate_content(prompt)
    return response.text

# ✅ Streamlit App 界面
st.set_page_config(page_title="科研搜索助手", layout="wide")
st.title("🔬 Gemini 科研搜索助手")
st.markdown("输入一个模糊或具体的科研问题，我们将自动帮你拆解问题、推荐数据库，并输出结构化总结。")

# 输入框
user_question = st.text_input("🧠 请输入你的科研问题：", value="")

# 触发按钮
if st.button("🔍 开始分析"):
    with st.spinner("思考中...请稍候"):
        try:
            result = research_search_assistant(user_question)
            st.markdown("### 📋 搜索结果如下：")
            st.markdown(result)
        except Exception as e:
            st.error(f"出错了：{e}")
else:
    st.info("👈 输入问题后点击“开始分析”按钮")

# 底部备注
st.markdown("---")
