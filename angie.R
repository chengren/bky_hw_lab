library(foreign)
library(readxl)
library(dplyr)
setwd('C:/Users/cheng/Downloads')
yourdata<-read.spss("Old_newW3  02-22-2018 wCSA for all.sav", use.value.labels = TRUE, to.data.frame = TRUE)
ls_name<-read_excel("CHLEW_to_import.xlsx")
var_name<-tolower(c(ls_name$`Variable name`))
colnames(yourdata)<-tolower(names(yourdata))
newdt<-yourdata%>%
  select(var_name)
length(unique(ls_name$`Variable name`))#80 unique names
write.dta(newdt,'newdt.dta')
