if (!require('readr')) install.packages('readr')
library(readr)
library(data.table)
library(magrittr)
library(dplyr)

initial.data <- read.csv("trip.csv")
summary(initial.data)


split.data <- initial.data %>% mutate('zip_5' = substr(trimws(zip_code),1,5))
dataset.part1 <- split.data %>% filter(zip_5 == '95113'| zip_5 == '94041'| zip_5 == '94107'| zip_5 == '94301'| zip_5 == '94063') 
remaining.data <- split.data %>% filter(zip_5 != '95113'& zip_5 != '94041'& zip_5 != '94107'& zip_5 != '94301'& zip_5 != '94063')
remaining.valid <- remaining.data %>% filter(substr(zip_5,1,1) == '9' & as.numeric(zip_5) >= 94000)
##check
#nrow(dataset.part1) + nrow(remaining.data)
dataset.part2 <- sample_n(remaining.valid, 250000 - nrow(dataset.part1))

final.data <- rbind(dataset.part1,dataset.part2)
final.data <- final.data %>% mutate('zip_5' = as.factor(zip_5))
summary(final.data)                                        


write.csv(final.data, 'trip250_random.csv')
