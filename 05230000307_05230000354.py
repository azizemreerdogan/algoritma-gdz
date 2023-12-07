#Constants are declared in Turkish Lira(TL)
SINGLE_TIME_ENERGY_FEE_INDUSTRIAL = 3.053828
SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 1.912220
SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 2.828414
SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_LOW= 0.482187
SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_HIGH = 1.132271
SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_FAMILY_MARTYRS = 0.061590 
SINGLE_TIME_ENERGY_FEE_AGRICULTURAL_ACTIVITIES =1.653096
SINGLE_TIME_ENERGY_FEE_LIGHTING = 2.595835
DAYTIME_PERIOD_ENERGY_FEE_INDUSTRY = 3.091933
DAYTIME_PERIOD_ENERGY_FEE_PUBLIC_PUBLIC_AND_PRIVATE_SECTOR_LOW = 2.858616
DAYTIME_PERIOD_ENERGY_FEE_PUBLIC_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 2.858616
DAYTIME_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW = 1.157700
DAYTIME_PERIOD_ENERGY_FEE_RESIDENTIAL_HIGH = 1.177700
DAYTIME_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES = 1.704822
PEAK_PERIOD_ENERGY_FEE_INDUSTRIAL = 4.909037
PEAK_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 4.588843
PEAK_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 4.588843
PEAK_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW = 2.083645
PEAK_PERIOD_ENERGY_FEE_RESIDENTIAL_HIGH = 2.083645
PEAK_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES = 2.800325
NIGHT_PERIOD_ENERGY_FEE_INDUSTRIAL = 1.625171
NIGHT_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 1.481641
NIGHT_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 1.481941
NIGHT_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW = 0.417225
NIGHT_PERIOD_ENERGY_FEE_RESIDENTIAL_HIGH = 0.417225
NIGHT_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES = 0.771882
UNIT_DISTRIBUTION_FEE_INDUSTRIAL = 0.647998
UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 0.878175
UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 0.878175
UNIT_DISTRIBUTION_FEE_RESIDENTIAL_LOW = 0.858883
UNIT_DISTRIBUTION_FEE_RESIDENTIAL_HIGH = 0.858883
UNIT_DISTRIBUTION_FEE_RESIDENTIAL_FAMILY_MARTYRS = 0.582521
UNIT_DISTRIBUTION_FEE_AGRICULTURAL_ACTIVITIES = 0.721579
UNIT_DISTRIBUTION_FEE_LIGHTING = 0.841099
ECT_RATE_INDUSTRIAL = 0.01
ECT_RATE_NOT_INDUSTRIAL = 0.05
VAT_RATE_INDUSTRIAL = 0.2
VAT_RATE_PUBLIC_AND_PRIVATE = 0.2
VAT_RATE_RESIDENTIAL = 0.1
VAT_RATE_AGRICULTURAL_ACTIVITIES = 0.1
VAT_RATE_LIGHTING = 0.2
DAILY_AVARAGE_UPPER_LIMIT_PUBLIC_AND_PRIVATE_SECTOR = 30
DAILY_AVARAGE_UPPER_LIMIT_FOR_RESIDENTIAL= 8


#Input validation func
def validation(x,text):
    number = float(input(f'{text}'))
    while number < x:
        print('Invalid')
        number = input(f'{text}')
    return number

#Consumption calculator func

def consumption(previous,current):
    return current - previous

#Total fee calculator
def feeCalc(preferredTariff): #The function should have a parameter beacuse the function is going to be used in calculating profit or loss
    #Two Stage
    if consumerType == 'Public and Private':
        if preferredTariff == 'Single':
            if limitExceed:
                totalFee = DAILY_AVARAGE_UPPER_LIMIT_PUBLIC_AND_PRIVATE_SECTOR*daysBetween*SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW + limitExceedAmount*SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH

            else:
                totalFee = totalConsumption*SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW
        else:

            daytimeFee = consumption(previousDaytime,currentDaytime)*DAYTIME_PERIOD_ENERGY_FEE_PUBLIC_PUBLIC_AND_PRIVATE_SECTOR_LOW
            peakFee = consumption(previousPeak,currentPeak)*PEAK_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW
            nightFee = consumption(previousNight,currentNight)*NIGHT_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW
            totalFee = daytimeFee + peakFee +  nightFee

    elif consumerType == 'Residential':
        if martyrOrVeteran:
            totalFee = totalConsumption * SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_FAMILY_MARTYRS
        else:
            if preferredTariff == 'Single':
                if limitExceed:
                    totalFee = DAILY_AVARAGE_UPPER_LIMIT_FOR_RESIDENTIAL*daysBetween*SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_LOW + limitExceedAmount*SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_HIGH
                    
                else:
                    totalFee = totalConsumption*SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_LOW
            else:
                
                daytimeFee = consumption(previousDaytime,currentDaytime)*DAYTIME_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW
                peakFee = consumption(previousPeak,currentPeak)*PEAK_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW
                nightFee = consumption(previousNight,currentNight)*NIGHT_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW
                totalFee = daytimeFee + peakFee +  nightFee

    elif consumerType == 'Industrial':
        if preferredTariff == 'Single':
            totalFee = totalConsumption*SINGLE_TIME_ENERGY_FEE_INDUSTRIAL
        else:
            daytimeFee = consumption(previousDaytime,currentDaytime)*DAYTIME_PERIOD_ENERGY_FEE_INDUSTRY
            peakFee = consumption(previousPeak,currentPeak)*PEAK_PERIOD_ENERGY_FEE_INDUSTRIAL
            nightFee = consumption(previousNight,currentNight)*NIGHT_PERIOD_ENERGY_FEE_INDUSTRIAL
            totalFee = daytimeFee + peakFee + nightFee

    elif consumerType == 'Agricultural':
        if preferredTariff == 'Single':
            totalFee = totalConsumption*SINGLE_TIME_ENERGY_FEE_AGRICULTURAL_ACTIVITIES
        else:
            daytimeFee = consumption(previousDaytime,currentDaytime)*DAYTIME_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES
            peakFee = consumption(previousPeak,currentPeak)*PEAK_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES
            nightFee = consumption(previousNight,currentNight)*NIGHT_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES
            totalFee = daytimeFee + peakFee + nightFee
    else: #Lightning
        totalFee = totalConsumption*SINGLE_TIME_ENERGY_FEE_LIGHTING

    #Return
    return totalFee   

#Tax and calculator
#(energy_feeECT+distribution_fee)VAT

def taxCalc(select,totalConsumptionFee):
    if consumerType == 'Industrial':
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_INDUSTRIAL
        taxECT = totalConsumptionFee*ECT_RATE_INDUSTRIAL
        taxVAT = ((taxECT+totalConsumptionFee) + unitDistribution)*VAT_RATE_INDUSTRIAL
        
    elif consumerType == 'Public and Private':
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH
        taxECT = (totalConsumptionFee)*ECT_RATE_NOT_INDUSTRIAL
        taxVAT = ((taxECT+totalConsumptionFee) + unitDistribution)*VAT_RATE_PUBLIC_AND_PRIVATE
        
    elif consumerType == 'Residential':
        taxECT = (totalConsumptionFee)*ECT_RATE_NOT_INDUSTRIAL
        if martyrOrVeteran:
            unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_RESIDENTIAL_FAMILY_MARTYRS
            taxVAT = ((taxECT+totalConsumptionFee) + unitDistribution)*VAT_RATE_RESIDENTIAL
            
        else:
            unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_RESIDENTIAL_LOW
            taxVAT = ((taxECT+totalConsumptionFee) + unitDistribution)*VAT_RATE_RESIDENTIAL
            
            
    elif consumerType == 'Agricultural':
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_AGRICULTURAL_ACTIVITIES
        taxECT = (totalConsumptionFee)*ECT_RATE_NOT_INDUSTRIAL
        taxVAT = ((taxECT+totalConsumptionFee) + unitDistribution)*VAT_RATE_AGRICULTURAL_ACTIVITIES
        
    else: #Lightning
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_LIGHTING
        taxECT = (totalConsumptionFee)*ECT_RATE_NOT_INDUSTRIAL
        taxVAT = ((taxECT+totalConsumptionFee) + unitDistribution)*VAT_RATE_LIGHTING
        
    
    #The function returns any of these taxes according to a parameter
    if select == 'ECT':
        return taxECT
    elif select == 'VAT':
        return taxVAT
    else: #Gives you the Unit Distribution Fee
        return unitDistribution
    

# Profit or loss calculator


def profitLossCalc(preferredTariff): 
    if preferredTariff == 'Single':
        newPreferredTariff = 'Multi'
    else:
        newPreferredTariff = 'Single'
    
    newTotalConsumptionFee = feeCalc(newPreferredTariff)
    newTotalECT  = taxCalc('ECT',newTotalConsumptionFee)
    newTotalVAT = taxCalc('VAT',newTotalConsumptionFee)
    newUnitDistribution = taxCalc('Distribution',newTotalConsumptionFee)
    newTotalInvoice = newTotalConsumptionFee + newUnitDistribution + newTotalECT + newTotalVAT
    difference = (newTotalInvoice - totalInvoice)   

    if difference > 0:
        profit = True

        profitLossAmount = difference
        print(f'The consumer has made a profit at amount of {profitLossAmount}')

    else:
        profit = False

        profitLossAmount = difference
        print(f'The consumer has made a loss at amount of {profitLossAmount}')
    
    return profit
    
#**********************************************************************************
#Inputs
#Counters
counterIndustrial = 0
counterPublic = 0
counterResidential = 0
counterAgricultural = 0
counterLightning = 0
allCustomersConsumption = 0
publicSingle = 0
publicDailyAverageCounter = 0
overusageIndustry = 0
maxResidentialDailyAverage = 0
maxTotalInvoice = 0
allCustomersGDZRevenue = 0
allCustomersECTRevenue = 0
allCustomersVATRevenue = 0
consumptionCounterIndustrial = 0
consumptionCounterResidential = 0
consumptionCounterPublic = 0
consumptionCounterAgricultural = 0
consumptionCounterLightning = 0
counterMultiLossConsumers = 0
counterOtherThanMartyrLightning = 0
while True:

    

    consumerNo = int(input('Please enter your consumer no, 0 to exit'))
    if consumerNo < 0:
        print('Invalid value')
    elif consumerNo == 0:
        break

    
    
    martyrOrVeteran = False
    preferredTariff = 'Single' #Default because when martyr or veteran an error occurs
    
    consumerType = input('Enter consumer type')
    while consumerType not in['I','i','P','p','R','r','A','a','L','l']:
        print()
        consumerType = input()

    match consumerType: #Consumer type check
        case 'I' | 'i':
            consumerType = 'Industrial'
        case 'P' | 'p':
            consumerType = 'Public and Private'
        case 'R' | 'r':
            consumerType = 'Residential'
        case 'A' | 'a':
            consumerType = 'Agricultural'
        case _:
            consumerType = 'Lightning'

        



    if consumerType == 'Residential':
        martyrOrVeteran = input('y or n')
        while martyrOrVeteran not in['Y','y','n','N']:
            print()
            martyrOrVeteran = input()
        if martyrOrVeteran == 'Y' or martyrOrVeteran == 'y':
            martyrOrVeteran = True
        else:
            martyrOrVeteran = False


    if (not martyrOrVeteran) and (consumerType != 'Lightning'):
        preferredTariff = input('Enter preferred tariff')
        while preferredTariff not in ['S','s','M','m']:
            print()
            preferredTariff = input()
        if preferredTariff == 'S' or preferredTariff == 's':
            preferredTariff = 'Single'
        else:
            preferredTariff = 'Multi'
        



    previousDaytime = validation(0,'Please enter previous daytime consumption')
    currentDaytime = validation(previousDaytime,'Please enter current daytime consumption')
    previousPeak = validation(0,'Enter previous Peak-time consumption')
    currentPeak = validation(previousPeak,'Please enter current Peak-time consumption')
    previousNight = validation(0,'Please enter previous Night-time consumption')
    currentNight = validation(previousNight,'Please enter current Night-time consumption')


    daysBetween = validation(1,'Please enter days between')
    totalConsumptionOfYear = validation(0,'Please enter total consumption made in the year')
    totalConsumption = consumption(previousDaytime,currentDaytime) + consumption(previousPeak,currentPeak) + consumption(previousNight,currentNight)

    dailyAverage = totalConsumption/daysBetween

    if consumerType == 'Public and Private':
        if dailyAverage <= 30: 
            limitExceed = False
        else:
            limitExceed = True
            limitExceedAmount = (dailyAverage-30)*daysBetween
        if preferredTariff == 'Single':
            publicSingle += 1
    elif consumerType == 'Residential':
        if totalConsumption / daysBetween <= 8:
            limitExceed = False
        else:
            limitExceed = True
            limitExceedAmount = (dailyAverage-8)*daysBetween





    totalConsumptionFee = feeCalc(preferredTariff)
    totalECT = taxCalc('ECT',totalConsumptionFee)
    totalVAT = taxCalc('VAT',totalConsumptionFee)
    totalUnitDistribution = taxCalc('Distrubution',totalConsumptionFee)

    totalInvoice = totalConsumptionFee + totalUnitDistribution + totalECT + totalVAT
    dailyAverage = totalConsumption/daysBetween
    if consumerType == 'Residential':
        if dailyAverage > maxResidentialDailyAverage: #Daily average max use finder
            maxResidentialDailyAverage = dailyAverage
            maxResidentialDailyAverageNo = consumerNo
            maxResidentialAverageConsumption = totalConsumption
            maxResidentialAverageBill = totalInvoice
    else:
        if totalInvoice > maxTotalInvoice: #Total bil max finder
            maxTotalInvoice = totalInvoice
            maxTotalInvoiceNo = consumerNo
            maxTotalInvoiceType = consumerType
            maxTotalInvoiceDailyAverage = dailyAverage
            maxTotalInvoiceConsumption = totalConsumption
    
    #Counters for each consumer types
    match consumerType:
        case 'Industrial':
            counterIndustrial+=1
            consumptionCounterIndustrial += totalConsumption
        case 'Residential':
            counterResidential+=1
            consumptionCounterResidential += totalConsumption
        case 'Public and Private':
            counterPublic+=1
            consumptionCounterPublic += totalConsumption
        case 'Agricultural':
            counterAgricultural+=1
            consumptionCounterAgricultural+= totalConsumption
        case 'Lightning':
            counterLightning+=1
            consumptionCounterLightning+= totalConsumption

           
        


    #Total statistics of all consumers by using counters
    
    allCustomersConsumption += totalConsumption
    if consumerType == 'Public and Private':
        publicDailyAverageCounter += dailyAverage
    
    allCustomersGDZRevenue += totalConsumptionFee + taxCalc('Distrubution',totalConsumptionFee)
    allCustomersECTRevenue += totalECT
    allCustomersVATRevenue  += totalVAT






        
    #Prints for each consumer

    print(f'Consumers number: {consumerNo}')
    print(f'Consumers type: {consumerType}')
    print(f'Consumers Daytime consumption: {consumption(previousDaytime,currentDaytime)}')
    print(f'Consumers Peak-time consumption: {consumption(previousPeak,currentPeak)}')
    print(f'Consumers Night-time consumption: {consumption(previousNight,currentNight)}')
    print(f'Consumers total periodic consumption: {totalConsumption}')
    print(f'Consumers total consumption fee: {round(totalConsumptionFee,2)}')
    print(f'Total ECT amount: {round(totalECT,2)}')
    print(f'Total VAT amount: {round(totalVAT,2)}')
    print(f'Total Invoice: {round(totalInvoice,2)}')

    
    if not(martyrOrVeteran) and consumerType != 'Lightning':
        profit = profitLossCalc(preferredTariff)
        
        counterOtherThanMartyrLightning += 1
        if preferredTariff == 'Multi' and not(profit):
            counterMultiLossConsumers += 1




    print(totalConsumptionOfYear)

    if totalConsumptionOfYear < 1000:
        freeConsumer = False
        print('The consumer does not deserve to be a free consumer')
    else:
        freeConsumer = True
        print('The consumer deserves to be a free consumer')
    if consumerType == 'Industrial' and (totalConsumptionOfYear> 10000 or totalInvoice > 100000): #Should do a TL conversion
        overusageIndustry += 1



totalConsumers = counterLightning + counterAgricultural + counterIndustrial + counterPublic + counterResidential
publicMulti = counterPublic - publicSingle
publicDailyAverage = publicDailyAverageCounter / counterPublic



#printing all of the information

print('For consumer type Industrial:')
print(f'Number of consumers: {counterIndustrial} ')
print(f'Percentage: {round(counterIndustrial/totalConsumers*100,2)}%')
print(f'Average electricty consumption: {consumptionCounterIndustrial/counterIndustrial}')
print(f'Total electricty consumption for Industrial {consumptionCounterIndustrial}')

print('For consumer type Public, Private and Other:')
print(f'Number of consumers: {counterPublic} ')
print(f'Percentage: {round(counterPublic/totalConsumers*100,2)}%')
print(f'Average electricty consumption: {consumptionCounterPublic/counterPublic}')
print(f'Total electricty consumption for Public, Private and Other {consumptionCounterPublic}')

print('For consumer type Residential:')
print(f'Number of consumers: {counterResidential} ')
print(f'Percentage: {round(counterResidential/totalConsumers*100,2)}%')
print(f'Average electricty consumption: {consumptionCounterResidential/counterResidential}')
print(f'Total electricty consumption for Residential {consumptionCounterResidential}')

print('For consumer type Agricultural Activites:')
print(f'Number of consumers: {counterAgricultural} ')
print(f'Percentage: {round(counterAgricultural/totalConsumers*100,2)}%')
print(f'Average electricty consumption: {consumptionCounterAgricultural/counterAgricultural}')
print(f'Total electricty consumption for Agricultural Activities {consumptionCounterAgricultural}')

print('For consumer type Lightning:')
print(f'Number of consumers: {counterLightning} ')
print(f'Percentage: {round((counterLightning/totalConsumers*100),2)}%')
print(f'Average electricty consumption: {round(consumptionCounterLightning/counterLightning,2)}')
print(f'Total electricty consumption for Lightning {round(consumptionCounterLightning,2)}')

print(f'Bornova\s total consumption is {round(allCustomersConsumption,2)}')

print(f'Number and percentage of public, private and other who prefer single{publicSingle}, {round((publicSingle/counterPublic*100),2)}%')
print(f'Number and percentage of public, private and other who prefer multi{publicMulti} {round((publicMulti/counterPublic*100),2)}%')


print(f'Number of Industry consumer who is over 10000kWh or 100000TL and their percentage: {overusageIndustry}, {overusageIndustry/counterIndustrial*100}%')
print(f'Consumer no of the residential type with the highest daily average consumption: {maxResidentialDailyAverageNo}')
print(f'This consumers daily average electricity usage: {round(maxResidentialDailyAverage,2)}')
print(f'This consumers total bill: {round(maxResidentialAverageBill,2)}')

print(f'Consumer no of highest total bill other than residential: {maxTotalInvoiceNo}')
print(f'Consumer type of this consumer: {maxTotalInvoiceType}')
print(f'Daily average electricity consumption of this consumer: {round(maxTotalInvoiceDailyAverage,2)}')
print(f'Total bill amount of this consumer: {round(maxTotalInvoice,2)}')

print(f'Total revenue earned by GDZ{round(allCustomersGDZRevenue,2)}')
print(f'Total revenue of municipality {round(allCustomersECTRevenue,2)}')
print(f'Total revenue of the state {round(allCustomersVATRevenue,2)}')

print(f'The percentage of those who made a loss {round((counterMultiLossConsumers/counterOtherThanMartyrLightning*100),2)}%')

























        

                
            




































            