class Htmloutuputer(object):
    def __init__(self):
        self.data=[]
    def collet_data(self, new_data):

        if new_data is None:
            return
        self.data.append(new_data)
    def out_put(self):
        fout=open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.data:
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'].encode('utf-8'))
            fout.write("<td>%s</td>"% data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"% data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()