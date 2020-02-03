library(haven)
Cats_Weight <- read_sav("C:/Users/cheng/Downloads/Cats Weight.sav")
#change your own working path
attr(Cats_Weight[[1]],'label')#test attr function
attr(Cats_Weight[[1]],'label')<-NULL # you can use the sameway to assign label
length(attr(Cats_Weight[[2]], 'label'))#test attr function length
ls_name=names(Cats_Weight)# change the cats_weight to your data frame name
ls <- c()

for(i in c(1:length(ls_name))){
  ls_lb=attr(Cats_Weight[[i]],'label')#change the cats_weight to your data frame name
  if (length(ls_lb)>1){
    print(i)
    print(ls_name[i])
  }
  ls <- append(ls,ls_lb) 
}
df_new <- as.data.frame(ls_name)# convert the list to the dataframe
df_new['question'] <- ls

