import pandas as pd
import sqlite3
import xlrd
import openpyxl
from datetime import datetime


date_today = datetime.today()

def insert_doc_list(proj_id, sub, code_doc):
  conn = sqlite3.connect('db.sqlite3')
  c = conn.cursor()

  qsl_datas = f"""
              INSERT INTO proj_documentlistproject(proj_name_id, subject_name_id, doc_name_pattern_id,type_doc_id,name_doc,page_type_id,page_format_id, created_at, update_at)
              VALUES ({proj_id}, {sub}, {code_doc},1,'-',1,1,'{date_today}','{date_today}');
              """
  c.execute(qsl_datas)
  conn.commit()
  conn.close()


def create_list(sub, proj_id, check_id):
  for a in check_id:
    print('>>>>>>>>>>>>DDDD', proj_id, sub[0], a)
    insert_doc_list(proj_id, sub[0], a)



  '''  for a in MyProjects:
    print('>>>>>>>>>>>AAAA', a.id)

  for a in Subjects:
    print('>>>>>>>>>>>BBBB', a)

  for a in ListDoc:
    print('>>>>>>>>>>>>CCCC', proj_id, sub[0], a.doc_name_pattern_id)
'''
  
    #for b in ListDoc:
      #print('>>>>>>>>>>>>CCCC', proj_id, sub[0], a)




























'''

#----------------------------------------
def read_sql_project(NAME): #Information Tables Read
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM proj_myproject
        WHERE project_name LIKE '%{NAME}%';
	"""
	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql_subject(NAME): #Information Tables Read
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM proj_subject
        WHERE subject_name LIKE '%{NAME}%';
	"""
	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql_documentlist(NAME): #Information Tables Read
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM proj_documentlist
        WHERE document_name LIKE '%{NAME}%';
	"""
	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


def read_sql_pagesheet(NAME): #Information Tables Read
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM proj_pagesheet
        WHERE name_sheet LIKE '%{NAME}%';
	"""
	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


#----------------------------------------
def insert_cotation(name_sub, code_sub):
  conn = sqlite3.connect('db.sqlite3')
  c = conn.cursor()

  qsl_datas = f"""
              INSERT INTO proj_cotations(proj_name, subject_name, doc_name_pattern, page_type, page_format, qt_page, qt_doc, qt_hh, cost_doc, created_at, update_at)
              VALUES ('{name_sub}', '{code_sub}','{date_today}','{date_today}');
              """
  c.execute(qsl_datas)
  conn.commit()
  conn.close()


df_cotation = pd.read_excel('media/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','COTATION_DOC')

for a in df_cotation.index:
  print('++++++++++ : ',a,read_sql_project(df_cotation['PROJETO'].loc[a])['id'], read_sql_subject(df_cotation['DISCIPLINA'].loc[a])['id'], read_sql_documentlist(df_cotation['DOCUMENTS_NAME'].loc[a])['id'], read_sql_pagesheet(df_cotation['TIPO_FOLHA'].loc[a])['id'], df_cotation['QT_FOLHA'].loc[a],df_cotation['QT_DOC'].loc[a],df_cotation['QT_HH'].loc[a],df_cotation['CUSTO_DOC'].loc[a])
  print('>>>> ', read_sql_project(df_cotation['PROJETO'].loc[a])['id'][0])
  print('>>>> ', read_sql_subject(df_cotation['DISCIPLINA'].loc[a])['id'][0])
  print('>>>> ', read_sql_documentlist(df_cotation['DOCUMENTS_NAME'].loc[a])['id'][0])
  print('>>>> ', read_sql_pagesheet(df_cotation['TIPO_FOLHA'].loc[a])['id'][0])
'''
  #insert_sub(df_cotation['SUBJECTS_NAME'].loc[a], df_cotation['SUBJECTS_COD'].loc[a])


#print(read_sql_project('Projeto Revitalização - Porto Novo'))




'''
def create_tables():

  def insert_sub(name_sub, code_sub):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO proj_subject(subject_name, subject_cod, update_at, created_at)
                VALUES ('{name_sub}', '{code_sub}','{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()

  def insert_doc_t(name_doc):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO proj_doct(name_doc, update_at, created_at)
                VALUES ('{name_doc}', '{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()

  def insert_doc_t(name_doc):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO proj_doct(name_doc, update_at, created_at)
                VALUES ('{name_doc}', '{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()

  def insert_doc_list(name_doc):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO proj_documentlist(document_name, update_at, created_at)
                VALUES ('{name_doc}', '{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()

  df_sub = pd.read_excel('media/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','SUBJECTS')
  df_doc_t = pd.read_excel('media/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DOC_TYPE')
  df_doc_list = pd.read_excel('media/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DOCUMENTS_NAME')

  for a in df_sub.index:
    insert_sub(df_sub['SUBJECTS_NAME'].loc[a], df_sub['SUBJECTS_COD'].loc[a])

  for a in df_doc_t.index:
    insert_doc_t(df_doc_t['DOC_TYPE'].loc[a])
  
  for a in df_doc_list.index:
    insert_doc_list(df_doc_list['DOCUMENTS_LIST'].loc[a])

create_tables()
print('Feito!')

'''














""" 

  def cria_proj(name_proj, name_company, comment):
    proj = form_proj.save(commit=False)
    proj.project_name = name_proj
    proj.company = name_company
    proj.comments = comment
    proj.save()

  def cria_paget(name_page):
    paget = form_paget.save(commit=False)
    paget.name_page = name_page
    paget.save()

  def cria_doct(name_doc):
    doct = form_doct.save(commit=False)
    doct.name_doc = name_doc
    doct.save()

  def cria_form(form_page):
    format = form_format.save(commit=False)
    format.name_format = form_page
    format.save()

  def cria_doc(doc_name, code_doc, format_doc, doc_type):
    doc = form_doc.save(commit=False)
    doc.documment_name = doc_name
    doc.doc_type_id = int(code_doc)
    doc.format_doc_id = int(format_doc)
    doc.doc_type_page_id = int(doc_type)
    doc.save()

  def cria_dis(name_dis):
    dis = form_dis.save(commit=False)
    dis.subject_name = name_dis
    dis.save()

  def cria_st(status):
    st = form_st.save(commit=False)
    st.doc_status = status
    st.save()


  def cria_act(acao):
    ac = form_ac.save(commit=False)
    ac.action_type = acao
    ac.save()

  def cria_func(function, cargo, contr):
    func = form_func.save(commit=False)
    func.emp_name = function
    func.emp_office = cargo
    func.emp_contrato = contr
    func.photo = ''
    func.save()

  df_proj = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','PROJECTS')
  df_doct = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DOC_TYPE')
  df_paget = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','PAGE_TYPE')
  df_doc = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','MODELO_DOCUMENTO')
  df_dis = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DISCIPLINAS')
  df_st = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','STATUS')
  df_ac = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','ACAO')
  df_emp = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','EMPLOYEES')
  df_form = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','FORMAT_PAGE')
      
  #PROJ---------------------------------------------------------
  for a in range(len(df_proj['NOME_PROJETO'])):
    name_proj = df_proj['NOME_PROJETO'].loc[a]
    name_company = df_proj['EMPRESA'].loc[a]
    comment = df_proj['COMENTARIO'].loc[a]
    cria_proj(name_proj, name_company, comment)

  #Paget---------------------------------------------------------
  for a in range(len(df_paget['TIPO_FOLHA'])):
    name_page = df_paget['TIPO_FOLHA'].loc[a]
    cria_paget(name_page)

  #Doct---------------------------------------------------------
  for a in range(len(df_doct['TIPO_DOC'])):
    name_doc = df_doct['TIPO_DOC'].loc[a]
    cria_doct(name_doc)

  #Dis----------------------------------------------------------
  for a in range(len(df_dis['NOME_DISCIPLINA'])):
    name_dis = df_dis['NOME_DISCIPLINA'].loc[a]
    cria_dis(name_dis)

  #st-----------------------------------------------------------
  for a in range(len(df_st['STATUS'])):
    status = df_st['STATUS'].loc[a]
    cria_st(status)

  #act----------------------------------------------------------
  for a in range(len(df_ac['ACAO'])):
    acao = df_ac['ACAO'].loc[a]
    cria_act(acao)

  #emp----------------------------------------------------------
  for a in range(len(df_emp['FUNCIONARIO'])):
    function = df_emp['FUNCIONARIO'].loc[a]
    cargo = df_emp['CARGO'].loc[a]
    contr = df_emp['CONTRATO'].loc[a]
    cria_func(function, cargo, contr)

  #format--------------------------------------------------------
  for a in range(len(df_form['FORMATO_FOLHA'])):
    form_page = df_form['FORMATO_FOLHA'].loc[a]
    cria_form(form_page)

  #Doc----------------------------------------------------------
  for a in range(len(df_doc['LISTA_DOCUMENTOS'])):
    doc_name = df_doc['LISTA_DOCUMENTOS'].loc[a]
    code_doc = int(df_doc['COD_DOC_TIPO'].loc[a])
    format_doc = df_doc['FORMATO'].loc[a]
    doc_type = int(df_doc['TIPO'].loc[a])
    cria_doc(doc_name, code_doc, format_doc, doc_type)


  return 'feito!'
 """