Data <- data.frame(
  X = sample (1:10),
  Y = sample(c("mon", "tues","wed","thurs", "fri","sat","sun"), 100, replace = TRUE),
  Z= sample (c("a","b","c"), 100, replace = TRUE),
  #ZZ = sample(c("yes", "no"), 100, replace = TRUE),
  ZZZ=runif(100, min=1, max=10000)
) 

Outcome <-
  structure(list(X = c(3L, 4L, 5L, 7L), Y = structure(c(3L, 3L, 
                                                        1L, 4L), .Label = c("fri", "sat", "tues", "wed"), class = "factor"), 
                 Z.1 = structure(c(3L, 3L, 2L, 2L), .Label = c("a", "b", "c"
                 ), class = "factor"), ZZ.1 = structure(c(1L, 2L, 1L, 1L), .Label = c("no", 
                                                                                      "yes"), class = "factor"), Z.2 = structure(c(2L, 1L, 3L, 
                                                                                                                                   1L), .Label = c("a", "b", "c"), class = "factor"), ZZ.2 = structure(c(2L, 
                                                                                                                                                                                                         1L, 1L, 2L), .Label = c("no", "yes"), class = "factor"), 
                 Z.3 = structure(c(1L, NA, NA, 2L), .Label = c("a", "c"), class = "factor"), 
                 ZZ.3 = structure(c(2L, NA, NA, 1L), .Label = c("no", "yes"
                 ), class = "factor")), row.names = c(NA, 4L), class = "data.frame")
Data <- as.data.frame(Data)


library(tidyverse)
df <- Data %>% 
  group_by(X) %>% 
  mutate(group_id = dense_rank(Z)) %>%
  ungroup() 

df$fund_no <- paste('fund_',df$group_id,sep='')
#df$group_id <- NULL

df2 <- df %>% 
  #this is very important#
  #if you did not assign unique value,it will return error with duplication
  mutate(group_id_2 = row_number())%>%
  spread(fund_no,ZZZ)#%>%
  select(-group_id_2)

for(i in c(1:max(df2$group_id))){
  label_name <- paste("fund_em_dum_",i,sep='')
  fund_name <-  paste("fund_",i,sep='')
  df2[,label_name] <- is.na(df2[,fund_name])%>% as.numeric()
}

