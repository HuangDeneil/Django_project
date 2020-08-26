<?php header("Content-Type:text/html; charset=utf-8"); ?>

<html>
<head>
<title>輸入 order input</title>
<link href="http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700,800|Open+Sans+Condensed:300,700" rel="stylesheet" />
<link href="../default.css" rel="stylesheet" type="text/css" media="all" />
<link href="../fonts.css" rel="stylesheet" type="text/css" media="all" />

<script src="../javascript/jquery-1.8.3.js"></script>


<style>
table {
  font-family: 微軟正黑體, sans-serif;
  border-collapse: collapse;
  width: 100%;
  color: #000000;
}

td, th {
  border: 1px solid ##dddddd ;
  text-align: left;
  padding: 2px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
.error {color: #FF0000;}

.textarea_typ1
{
    border:1px solid #999999;
    width:95%;
    margin:5px 0;
    padding:1%;
}

.input_type1
{
    border:1px solid #999999;
    width:50%;
    margin:6px 0;
    padding:1%;
}

.select_type1
{
    border:1px solid #999999;
    width:50%;
    margin:5px 0;
    padding:1%;
}
</style  style="width:100%">

</head>


<!--- 
#######################################################################
###################*####*#####***#####*****######*****################
###################*####*###*#####*########*#####*####*###############
###################******##*********###*****#####*#####*##############
###################*####*###*#########*####**####*###*################
###################*####*####*****######***##*###****#################
#######################################################################
--->

<body>
<div id="logo" class="container">
  <a href="../index.html" class="button" style="font-family:微軟正黑體;text-transform:initial;font-size:120%">Back</a>
  <h1 style="font-family:微軟正黑體;text-transform:initial;font-size:300%">物種資料庫<span>Loacl web system</span>
  <h1 style="font-family:微軟正黑體;text-transform:initial;font-size:200%" >新增資料</h1></h1>
</div>


<?php
/*
########################################################
#################### 表格資訊填寫  ######################
########################################################
*/
?>

  
<!--- Table region  --->
<div id="wrapper" class="container">
  <form name="table_value" method="POST" action="query.php">
  <p><span style="font-family:微軟正黑體;text-transform:initial;font-size:200%" class="error">&ensp;&ensp;* 必填欄位</span><p>
  
  <h2 style="font-family:微軟正黑體;text-transform:initial;font-size:200%">基礎資訊</h2>
  <svg height="7" width="1200"><line x1="0" y1="0" x2="1300" y2="0" style="stroke:rgb(0,150,255);stroke-width:2" /></svg>
 <table>
    <tr>
      <td>&ensp;物種編號 : </br><p>&ensp;id</p>
      <td><input class=input_type1 type="text" name="id" >(本欄未填寫則自動生成) </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>&ensp;物種名 : </br>&ensp;Organism name</td>
      <td><input class=input_type1 type="text" name="organism_name" id="organism_name" ><span class="error">* </span></td>
      <td>&ensp;物種中文名 : </br>&ensp;Chinese name</td>
      <td><input class=input_type1 type="text" name="chinese_name" id="chinese_name" ></td>
    </tr>
  </table>

    </br></br>

  <h2 style="font-family:微軟正黑體;text-transform:initial;font-size:200%">分類資訊</h2>
  <svg height="7" width="1200"><line x1="0" y1="0" x2="1300" y2="0" style="stroke:rgb(0,150,255);stroke-width:2" /></svg>

  <table>
    <tr>
        <td>&ensp;屬名:</br>&ensp;Genus</td>
        <td><input class=input_type1 type="text" name="genus" id="genus" ><span class="error">* </span>
          <p>ex: <i>Klebsiella, Acinetobacter</i></p>
        </td>
        <td>&ensp;大分類:</br>&ensp;Top type:</td>
        <td>
          <select class=select_type1 name="type">
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value=""></option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="bacteria">bacteria</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="archaea">archaea</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="fungi">fungi</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="virus">virus</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="parasite">parasite</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="Mycoplasma/Chlamydia/Rickettsia">Mycoplasma/Chlamydia/Rickettsia</option>
          </select>  <span class="error">* </span>
          <p>bacteria, archaea, fungi, virus, parasite, Mycoplasma/Chlamydia/Rickettsia</p>
        </td>
    </tr>
    <tr>
        <td>&ensp;種名:</br>&ensp;Species</td>
        <td><input class=input_type1 type="text" name="species_name" id="species_name" ><span class="error">* </span>
          <p>ex: <i>Klebsiella pneumoniae, </br>Acinetobacter baumannii</i></p>
        </td>
        <td>&ensp;關鍵字:</br>&ensp;key word</td>
        <td>
          </br>
          <h3>Aerobic/anaerobic:</h3>
          <input type="checkbox" id="Strictly aerobic" name="Strictly aerobic" value="Strictly aerobic">
          <label for="Strictly aerobic">Strictly aerobic</label>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="Aerobic" name="Aerobic" value="Aerobic">
          <label for="Aerobic">Aerobic</label>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="Obligate_aerobe" name="Obligate_aerobe" value="Obligate_aerobe">
          <label for="Obligate_aerobe">Obligate_aerobe</label></br>
          <input type="checkbox" id="Facultative anaerobic" name="Facultative anaerobic" value="Facultative anaerobic">
          <label for="Facultative anaerobic">Facultative anaerobic</label>&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="Microaerophiles" name="Microaerophiles" value="Microaerophiles">
          <label for="Microaerophiles">Microaerophiles</label>&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="Aerotolerant" name="Aerotolerant" value="Aerotolerant">
          <label for="Aerotolerant">Aerotolerant</label>&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="Anaerobic" name="Anaerobic" value="Anaerobic">
          <label for="Anaerobic">Anaerobic</label>
          </br></br>
           
          
          <h3>Pathogenic:</h3>
          <input type="checkbox" id="pathogen" name="pathogen" value="pathogen">
          <label for="pathogen">pathogen</label>&ensp;&ensp;
          <input type="checkbox" id="opportunistic pathogen" name="opportunistic pathogen" value="opportunistic pathogen">
          <label for="opportunistic pathogen">opportunistic pathogen</label>&ensp;
          <input type="checkbox" id="plant pathogen" name="plant pathogen" value="plant pathogen">
          <label for="plant pathogen">plant pathogen</label>&ensp;
          <input type="checkbox" id="unkown pathogenic" name="unkown pathogenic" value="unkown pathogenic">
          <label for="unkown pathogenic">unkown pathogenic</label>&ensp;
          <br><br>

          <h3>Flora/environmental:</h3>
          <input type="checkbox" id="normal flora" name="normal flora" value="normal flora">
          <label for="normal flora">normal flora</label>
          <input type="checkbox" id="environmental" name="environmental" value="environmental">
          <label for="environmental">environmental</label>
          <br><br>
          
          <h3>Position:</h3>
          <input type="checkbox" id="oral" name="oral" value="oral">
          <label for="oral">oral</label>&ensp;&ensp;&ensp;
          <input type="checkbox" id="gut" name="gut" value="gut">
          <label for="gut">gut</label>&ensp;&ensp;&ensp;
          <input type="checkbox" id="skin" name="skin" value="skin">
          <label for="skin">skin</label>&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="vaginal" name="vaginal" value="vaginal">
          <label for="vaginal">vaginal</label>&ensp;&ensp;&ensp;
          <input type="checkbox" id="respiratory" name="respiratory" value="respiratory">
          <label for="respiratory">respiratory</label>&ensp;
          <br><br>

          <h3>Extrime type:</h3>
          <input type="checkbox" id="extrime" name="extrime" value="extrime">
          <label for="extrime">extrime</label>&ensp;&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="acidophilic" name="acidophilic" value="acidophilic">
          <label for="acidophilic">acidophilic</label>&ensp;&ensp;&ensp;&ensp;
          <input type="checkbox" id="thermophilic" name="thermophilic" value="thermophilic">
          <label for="thermophilic">thermophilic</label>&ensp;&ensp;&ensp;
          </br></br>
          
          <input type="checkbox" id="unkown" name="unkown" value="unkown">
          <label for="unkown">unkown</label><br>
          </br><p>others:
          <textarea class=textarea_typ1 type="text" name="key_word" id="key_word" rows="3" cols="80"></textarea><span class="error">* </span>
          </p>
        </td>
    </tr>
    <tr>
    <td>&ensp;格蘭氏染色:</br>&ensp;Gram stain:</td>
        <td>
          <select class=select_type1 name="gram_stain">
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value=""></option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="positive">positive</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="negative">negative</option>
          </select>  <span class="error">* </span>
        </td>
    <td>&ensp;樣品來源</br>&ensp;Sample type:</td>
        <td>
          <select class=select_type1 name="sample_type">
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value=""></option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="positive">positive</option>
            <option style="font-family:微軟正黑體;text-transform:initial;font-size:120%" value="negative">negative</option>
          </select>  <span class="error">* </span>
        </td>
    </tr>
    <tr>
        <td>&ensp;Halos id:</td>
        <td><input class=input_type1 type="text" name="Halos_id" ><p></p></td>
        <td>&ensp;taxid:</td>
        <td><input class=input_type1 type="text" name="taxid"></td>
    </tr>
    <tr>
      <td>&ensp;資訊來源:</br>&ensp;source</td>
      <td><input class=input_type1 type="text" name="source"><p>ex: Halos, from someone</p></td>
      <td>&ensp;species_taxid:</td>
      <td><input class=input_type1 type="text" name="species_taxid"></td>
    <tr>
  </table>
  <table>
    <tr>
      <td>&ensp;物種描述:</br>&ensp;Description</td>
      <td><textarea class=textarea_typ1 type="text" name="Description" id="Description" rows="5" cols="130"></textarea><span class="error">* </span></td>
    </tr>
  </table>
  </br>
      
  <h2 style="font-family:微軟正黑體;text-transform:initial;font-size:200%">文獻(reference):</h2>
  <svg height="7" width="1200"><line x1="0" y1="0" x2="1300" y2="0" style="stroke:rgb(0,150,255);stroke-width:2" /></svg>
  <table>
    <tr>
      <td>文獻1</br>reference1:</td>
      <td><textarea class=textarea_typ1 type="text" name="reference1" id="reference1" rows="2" cols="130" id="order_form"></textarea><span class="error">* </span></td>
    </tr>
    <tr>
      <td>文獻2</br>reference2:</td>
      <td><textarea class=textarea_typ1 type="text" name="reference2" rows="2" cols="130"></textarea></td>
    </tr>
    <tr>
      <td>文獻3</br>reference3:</td>
      <td><textarea class=textarea_typ1 type="text" name="reference3" rows="2" cols="130"></textarea></td>
    </tr>
    <tr>
      <td>文獻4</br>reference4:</td>
      <td><textarea class=textarea_typ1 type="text" name="reference4" rows="2" cols="130"></textarea></td>
    </tr>
    <tr>
      <td>文獻5</br>reference5:</td>
      <td><textarea class=textarea_typ1 type="text" name="reference5" rows="2" cols="130"></textarea></td>
    </tr>
  </table>
  </br>
  </br>

  <h2 style="font-family:微軟正黑體;text-transform:initial;font-size:200%">來源資訊:</h2>
  <svg height="7" width="1200"><line x1="0" y1="0" x2="1300" y2="0" style="stroke:rgb(0,150,255);stroke-width:2" /></svg>
  <table>
    <tr>
      <td>資料來源</br>data source</td>
      <td><input class=input_type1 type="text" name="data_source" id="data_source" rows="2" cols="130" ></textarea>
        <p>ex: NCBI、PATRIC、EupathDB、FDA-ARGOS</p>
      </td>
    </tr>
    <tr>
      <td>資料基因狀況</br>data status</td>
      <td><input class=input_type1 type="text" name="data_status" id="data_status" rows="2" cols="130" ></textarea>
        <p>ex: complete genome, chromosome, scaffold, contig</p>
      </td>
    </tr>
  </table>
<script>
    var order_form = $("#name").value;
    var source_name = document.getElementById("genus").value;
    var source_phone = document.getElementById("type").value;
    var arrive_name = document.getElementById("key_word").value;
    var arrive_phone = document.getElementById("Description").value;
    var arrive_address = document.getElementById("reference1").value;

    if( document.getElementById("name").value === "" ){ document.write("") }
    else if( source_name === "" ){ }
    else if( source_phone === "" ){ }
    else if( arrive_name === "" ){ }
    else if( arrive_phone === "" ){ }
    else if( arrive_address === "" ){  }
    else{
      document.write("test");alert("test");
      }
    
</script>
<p>
<?php
  for($i=0;$i<60;$i++) {echo "&ensp;"; }
  echo '<input class="button" style="font-family:微軟正黑體;text-transform:initial;font-size:300%" type="submit" value="送出">'; 
  echo '<input class="button" style="font-family:微軟正黑體;text-transform:initial;font-size:300%" type="reset" value="清除">';
?>
</p></br>
</div>
</body>
</html>


