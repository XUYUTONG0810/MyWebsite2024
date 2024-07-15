# 如果要运行图片处理工具
# 在run后面输入:(空格)--server.enableXsrfProtection=false
'''我的主页'''
import streamlit as st
from PIL import Image,ImageOps,ImageFilter,ImageDraw
import matplotlib.pyplot as plt
import change_picture as cp

page = st.sidebar.radio('我的首页', ['我的音乐推荐', '我的兴趣学科', '我的图片处理工具', '我的智慧词典', '我的留言区'])


# 音乐加载
def music_loading(music):
    with open(music, 'rb') as f:
        mp3 = f.read()
    st.audio(mp3, format = 'audio/mp3', start_time = 0)

    
# 页面 
def page_1():
    # 我的音乐推荐
    st.write('# :musical_note: :blue[我的音乐推荐]')
    
    st.write('我喜欢电子音乐，节奏能将一切不愉快甩开')
    music_loading('Nevada.mp3')
    st.write('*《Nevada》*')
    
    st.write('我也喜欢纯音乐，不管是钢琴、小提琴还是电子，旋律都能在心中打动我、振奋我')
    music_loading('Sunburst.mp3')
    st.write('*《Sunburst》*')
    
    st.write('我还喜欢古风乐曲（当然包含古风纯音乐）')
    music_loading('China X.mp3')
    st.write('*《China X》*')
    
    st.write('我喜欢震撼心灵的史诗音乐')
    music_loading('Last Reunion.mp3')
    st.write('*《Last Reunion》*')

    st.write('-'*50)
    st.write(':orange[你喜欢我推荐的音乐吗？下面就是我最喜欢的音乐软件（的网页）]')
    st.link_button('网易云音乐', 'https://music.163.com/#')

def page_2():
    # 我的图片处理工具
    st.write('# :sunglasses:图片处理小程序')
    uploaded_file = st.file_uploader('上传图片', type = ['png','jpeg','jpg'])
    if uploaded_file:
        name = uploaded_file.name
        type = uploaded_file.type
        size = uploaded_file.size
        img = Image.open(uploaded_file)
        
        st.write('*不要选择四种图片变色中的多个，否则可能达不到预期*')
        l1, l2= st.columns([1, 1])
        with l1:
            cc1 = st.toggle('图片变色RBG')
            cc2 = st.toggle('图片变色GRB')
            gr = st.toggle('灰度')
            iv = st.toggle('反色')
        with l2:
            cc3 = st.toggle('图片变色BRG')
            cc4 = st.toggle('图片变色BGR')
            ga = st.toggle('模糊')
            al = st.toggle('透明')
        if al:
            a = st.slider('你想要的透明度是：', 0, 255, 0)

        st.image(img)
        st.write('*原图*')
        img_result = img
        if st.button('开始图片处理'):
            if cc1:
                img_result = cp.change_colour(img_result, 0, 2, 1)
            if cc2:
                img_result = cp.change_colour(img_result, 1, 0, 2)
            if cc3:
                img_result = cp.change_colour(img_result, 2, 0, 1)
            if cc4:
                img_result = cp.change_colour(img_result, 2, 1, 0)
            if gr:
                img_result = cp.gray(img_result)
            if iv:
                img_result = cp.invert(img_result)
            if ga:
                img_result = cp.gaussian(img_result)
            if al:
                img_result = cp.alpha(img_result, a)
            
            st.image(img_result)
            st.write('*处理后图片*')
        

def page_3():
    # 我的智慧词典
    st.write('# :book: :blue[智能词典]')

    # 遍历词典
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')

    word_dict = {}
    for j in word_list:
        word_dict[j[1]] = [j[0], j[2]]
    # 查询次数
    with open('check_out_time.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict = {}
    if len(times_list[0]) > 1:
        for j in times_list:
            times_dict[j[0]] = int(j[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    if word in word_dict:
        st.subheader(word_dict[word][1])
        # 更新次数
        n = word_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write('查询次数:' + str(times_dict[n]))

        with open('check_out_time.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
           
def page_4():
    # 我的留言区
    st.write('# :email: :blue[我的留言区]')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    if len(messages_list[0]) > 1:
        for j in messages_list:
            if j[0] == '作者':
                with st.chat_message('🔥'):
                    st.text(j[0] + ':' + j[1])
            elif j[0] == '其他（男）':
                with st.chat_message('👦'):
                    st.text(j[0] + ':' + j[1])
            elif j[0] == '其他（女）':
                with st.chat_message('👧'):
                    st.text(j[0] + ':' + j[1])
    # 新增留言
    name = st.selectbox('我是……', ['作者', '其他（男）', '其他（女）'])
    st.write('*:orange[如果想要一个此网站中的名字和头像，在这里打出想要的名字和头像，马上就会添加]*')
    new_message = st.text_input('想要说的话……')
    st.write('*:orange[留言加载不出来？请刷新一下]*')
    if st.button('留言'):
        with open('leave_messages.txt', 'a', encoding='utf-8') as f:
            message = ''
            message += name + '#' + new_message + '\n'
            f.write(message)

def page_5():
    # 我的兴趣学科
    st.write('# :earth_asia: :blue[我爱地理学]')
    st.write('刚接触地理这个学科时，我便被深深吸引，我想记住每一幅地图，我想了解我们脚下星球的一切知识')
    
    # 小知识问答
    st.write('-'*50)
    st.write('我们来做一些简单的地理小知识的问答吧。')
    st.image('挪威1.jpg')
    
    season = st.text_input('这是什么季节（请输入英文）')
    country = st.radio('这最有可能是什么国家？', ['印度', '埃及', '挪威', '巴西'])
    climate = st.radio('这最有可能是什么气候？', ['热带沙漠气候', '亚热带季风气候', '地中海气候', '极地气候'])

    st.write('这有可能出现什么现象（多选）')
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        h1 = st.checkbox('极昼')
    with col2:
        h2 = st.checkbox('极夜')
    with col3:
        h3 = st.checkbox('太阳直射')

    if st.button('提交答案'):
        if season == 'winter':
            st.snow()
            if country == '挪威' and climate == '极地气候' and h1 and h2:
                st.write('回答正确')
            else:
                st.write('回答错误')
        else:
            st.write('回答错误')
            

if page == '我的音乐推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的兴趣学科':
    page_5()



