from spire.doc import Document, FileFormat
# 创建文档对象
doc = Document()
# 加载md文件
doc.LoadFromFile("Homework3_Readme.md", FileFormat.Markdown)
# 保存为Word文件
doc.SaveToFile("Homework3_Readme.docx", FileFormat.Docx2016)
doc.Close()