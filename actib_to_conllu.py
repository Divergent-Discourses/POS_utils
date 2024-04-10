def actib_to_conllu(fname):
    
    fhandle = fname[:-4]

    with open(fname) as f:
        text = f.read()

    text = text.split('<utt>')
    text = [i.strip() for i in text]

    tibetan_pattern = r'[\u0F00-\u0FFF]+'
    tibetan_words = [re.findall(tibetan_pattern, t) for t in text]
    tibetan_sentences = [''.join(t) for t in tibetan_text]
    
    tag_pattern = r'/(?P<tag>[^/\s]+)'
    actib_tags = [re.findall(tag_pattern, t) for t in text]
   
    words_tags = []
    for i, j in zip(tibetan_words, actib_tags):
        words_tags.append(dict(zip(i, j)))
    
    with open('{}.conllu'.format(fhandle), 'w') as outfile:
        sentence_counter = 1
        for i in range(len(text)):
            
            token_counter = 0
            outfile.write('# sent_id = {}:{}\n'.format(fhandle, sentence_counter))
            outfile.write('# {}\n'.format(tibetan_sentences[i]))
            
            for word, tag in words_tags[i].items():
                try:
                    outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t\n'.format(
                        token_counter+1, word, '_', actib_UD_lookup[tag], '_', tag, 0, 'root', '_', 'SpaceAfter=No'
                    )
                                 )
                    token_counter += 1
                except:
                    
                    if tag[0] == 'v':
                        outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t\n'.format(
                        token_counter+1, word, '_', 'VERB', '_', tag, 0, 'root', '_', 'SpaceAfter=No'
                    )
                                 )
                        token_counter += 1
                    
                    elif tag[0] == 'p':
                        outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t\n'.format(
                        token_counter+1, word, '_', 'PRON', '_', tag, 0, 'root', '_', 'SpaceAfter=No'
                    )
                                 )
                        token_counter += 1
                    
                    elif tag[:1] == 'cv':
                        outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t\n'.format(
                        token_counter+1, word, '_', 'ADP', '_', tag, 0, 'root', '_', 'SpaceAfter=No'
                    )
                                 )
                        token_counter += 1
                        
                
                
            sentence_counter += 1
            outfile.write('\n\n')