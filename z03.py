def main():
    items = 10
    offset = 0
    qid = '20894671'
    f = open('test.txt','a+')
    for  i in range (0,20):
          offset = i * items
          print(offset)
          print('page', i, 'num', offset)
          url = 'https://www.zhihu.com/api/v4/questions/'+qid+'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit='+str(items)+'&offset='+str(offset)+'&platform=desktop&sort_by=default'
          f.write(url+'\r\n')
    f.close()
if __name__=="__main__":
   main()