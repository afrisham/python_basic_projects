def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! i am your python chatbot. i am able to help you with python information.How can I assist you today?"
    elif "python " in user_input:
        return "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used for web development, data analysis, artificial intelligence, scientific computing,  data science and more. It has a large standard library and a vibrant community that contributes to its extensive ecosystem of third-party packages."
    elif "data science" in user_input:
        return "Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data. It combines aspects of statistics, computer science, machine learning, deep learning  and domain expertise to analyze and interpret complex data sets. Data scientists use various tools and techniques to clean, process, and visualize data, as well as to build predictive models and make data-driven decisions."  
    elif "machine learning" in user_input or "ML" in user_input or "ml" in user_input:
        return "Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computers to perform tasks without explicit programming. It involves training models on data to make predictions or decisions. Machine learning is widely used in various applications, including image recognition, natural language processing, and autonomous vehicles."
    elif "deep learning" in user_input or "DL" in user_input or "dl" in user_input:
        return "Deep learning is a subset of machine learning that uses neural networks with multiple layers (hence 'deep') to model complex patterns in data. It has been particularly successful in tasks such as image and speech recognition, natural language processing, and game playing. Deep learning models can automatically learn features from raw data, making them powerful for handling large and unstructured datasets."
    elif "invention of python"  or " founder" in user_input:
        return "Python was invented by Guido van Rossum and was first released in 1991. It was designed to be easy to read and write, with a focus on code readability and simplicity. Python's design philosophy emphasizes code readability and a syntax that allows programmers to express concepts in fewer lines of code compared to other programming languages. "  
    elif "python features" in user_input:
        return "Some of the key features of Python include: 1. Easy to learn and use: Python has a simple syntax that is easy to read and write, making it an excellent choice for beginners. 2. Interpreted language: Python is an interpreted language, which means that code can be executed line by line without the need for compilation. 3. Dynamically typed: Python does not require explicit declaration of variable types, allowing for more flexibility in coding. 4. Large standard library: Python comes with a vast standard library that provides modules and functions for various tasks, such as file handling, regular expressions, and web development. 5. Cross-platform compatibility: Python can run on various operating systems, including Windows, macOS, and Linux. 6. Support for multiple programming paradigms: Python supports procedural, object-oriented, and functional programming styles, allowing developers to choose the best approach for their projects."
    elif " futures scope" in user_input:
        return "The future scope of Python is very promising. With its versatility and ease of use"
    elif "use of python" in user_input:
        return "Python is used in a wide range of applications, including: 1. Web development: Python frameworks like Django and Flask are popular for building web applications. 2. Data analysis and visualization: Libraries such as Pandas, NumPy, and Matplotlib are widely used for data manipulation and visualization. 3. Machine learning and artificial intelligence: Python has become the go-to language for machine learning and AI development, with libraries like TensorFlow, Keras, and Scikit-learn. 4. Scientific computing: Python is used in scientific research for tasks such as simulations, data analysis, and visualization. 5. Automation and scripting: Python's simplicity makes it ideal for automating repetitive tasks and writing scripts to manage systems or perform data processing."
    elif "data analysis" in user_input:
        return "Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making. It involves various techniques and tools to analyze data sets, identify patterns, and extract insights. Data analysis can be performed using statistical methods, machine learning algorithms, and data visualization techniques. It is widely used in various fields such as business, healthcare, finance, and social sciences to make informed decisions based on data."
    elif "data visualization" in user_input:
        return "Data visualization is the graphical representation of information and data. It uses visual elements such as charts, graphs, and maps to help people understand complex data sets and identify patterns, trends, and outliers. Data visualization is an essential part of data analysis, as it allows analysts to communicate their findings effectively and make data-driven decisions. Popular tools for data visualization include Matplotlib, Seaborn, and Tableau."
    elif "python libraries" in user_input:
        return "Some popular Python libraries include: 1. NumPy: A library for numerical computing and array manipulation. 2. Pandas: A library for data manipulation and analysis. 3. Matplotlib: A library for creating static, animated, and interactive visualizations. 4. Scikit-learn: A library for machine learning and data mining. 5. TensorFlow: An open-source library for machine learning and deep learning. 6. Keras: A high-level neural networks API that runs on top of TensorFlow. 7. Flask: A micro web framework for building web applications."
    else:
        return "I'm sorry, I don't have information on that topic due to some limitations. Please ask about Python, data science, machine learning, deep learning, or any related topics."
      
    
     while True:
         print("your python_info chatbot is ready type bye or exit to stop disscusion ")
        user_input = input("You: ")
        response = chatbot_response(user_input)
        if "bye" in user_input.lower() or "goodbye" in user_input.lower() or "exit" in user_input.lower() or "quit" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        print ("thanks for chatting with me. if you have any question about python or data science or machine learning or deep learning then ask me. i will try to give you the best answer. see you later!")
    
