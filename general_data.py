from bs4 import BeautifulSoup
import requests

class GeneralData(object):
    def __init__(self, filename):
        '''
        filename: Name of file to save data to
        '''
        self.base_url = "http://www.scpwiki.com/"
        self.filename = filename
    
    def run(self):
        '''
        Saves the rating and number of comments for each scp 
        on the wiki.
        '''
        with open(self.filename, "w") as f:
            f.write("scp_number rating comments\n")

            for idx in range(1, 6000):
                self._get_for_page(idx, f)

    def _get_for_page(self, idx, writefile, retry_count=0):
        '''
        idx: scp number
        writefile: file to write to
        '''
        if (idx % 10 == 0):
            print("Passed SCP-{0:03}".format(idx))
        
        try:
            page = requests.get(self.base_url + "scp-{0:03}".format(idx))
            root_page = BeautifulSoup(page.content, "html.parser")
            rating = root_page.find(id="pagerate-button")
            comments = root_page.find(id="discuss-button")

            if (rating is None or comments is None):
                return

            rating_str = rating.text
            comments_str = comments.text
            
            # Format of rating_str is "Rate (+495)"
            rate_num_temp = rating_str.split("(")[1].split(")")[0]
            if rate_num_temp.startswith("+") or rate_num_temp.startswith("-"):
                rate_num_temp = rate_num_temp[1:]
            if (rate_num_temp == ""):
                # skip SCPs that are behind some sort of content wall
                writefile.write("{0}\n".format(idx))
                return

            rate_num = int(rate_num_temp)
            # Format of comments_str is "Discuss (54)"
            comments_num = int(comments_str.split("(")[1].split(")")[0])

            writefile.write("{0} {1} {2}\n".format(idx, rate_num, comments_num))

        except ConnectionResetError as e:
            if retry_count > 5:
                raise e
            else:
                print("Connection reset, retry attempt {0}".format(retry_count + 1))
                this._get_for_page(idx, writefile, retry_count + 1)

if __name__=="__main__":
    GeneralData("rdata/data.txt").run()