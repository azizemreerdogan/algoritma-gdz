#Constants are declared in Turkish Lira(TL)
SINGLE_TIME_ENERGY_FEE_INDUSTRIAL = 3.053828
SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 1.912220
SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 2.828414
SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_LOW= 48.2187
SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_HIGH = 113.2271
SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_FAMILY_MARTYRS = 6.1590 
SINGLE_TIME_ENERGY_FEE_AGRICULTURAL_ACTIVITIES =165.3096
SINGLE_TIME_ENERGY_FEE_LIGHTING = 259.5835
DAYTIME_PERIOD_ENERGY_FEE_INDUSTRY = 309.1933
DAYTIME_PERIOD_ENERGY_FEE_PUBLIC_PUBLIC_AND_PRIVATE_SECTOR_LOW = 285.8616
DAYTIME_PERIOD_ENERGY_FEE_PUBLIC_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 285.8616
DAYTIME_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW = 115.7700
DAYTIME_PERIOD_ENERGY_FEE_RESIDENTIAL_HIGH = 117.7700
DAYTIME_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES = 170.4822
PEAK_PERIOD_ENERGY_FEE_INDUSTRIAL = 490.9037
PEAK_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 148.1941
PEAK_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 458.8843
PEAK_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW = 208.3645
PEAK_PERIOD_ENERGY_FEE_RESIDENTIAL_HIGH = 208.3645
PEAK_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES = 280.0325
NIGHT_PERIOD_ENERGY_FEE_INDUSTRIAL = 162.5171
NIGHT_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 148.1641
NIGHT_PERIOD_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 148.1941
NIGHT_PERIOD_ENERGY_FEE_RESIDENTIAL_LOW = 41.7225
NIGHT_PERIOD_ENERGY_FEE_RESIDENTIAL_HIGH = 41.7225
NIGHT_PERIOD_ENERGY_FEE_AGRICULTURAL_ACTIVITIES = 77.1882
UNIT_DISTRIBUTION_FEE_INDUSTRIAL = 64.7998
UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 87.8175
UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 87.8175
UNIT_DISTRIBUTION_FEE_RESIDENTIAL_LOW = 85.8883
UNIT_DISTRIBUTION_FEE_RESIDENTIAL_HIGH = 85.8883
UNIT_DISTRIBUTION_FEE_RESIDENTIAL_FAMILY_MARTYRS = 58.2521
UNIT_DISTRIBUTION_FEE_AGRICULTURAL_ACTIVITIES = 72.1579
UNIT_DISTRIBUTION_FEE_LIGHTING = 84.1099
ECT_RATE_INDUSTRIAL = 0.01
ECT_RATE_NOT_INDUSTRIAL = 0.05
#ECT_RATE_PUBLIC_AND_PRIVATE_SECTOR_LOW = 0.05
#ECT_RATE_PUBLIC_AND_PRIVATE_SECTOR_HIGH = 0.05
#ECT_RATE_RESIDENTIAL_LOW = 0.05
#ECT_RATE_RESIDENTIAL_HIGH = 0.05
#ECT_RATE_RESIDENTIAL_FAMILY_MARTYRS = 0.05
#ECT_RATE_AGRICULTURAL_ACTIVITIES = 0.05
#ECT_RATE_LIGHTING = 0.05
VAT_RATE_INDUSTRIAL = 0.2
VAT_RATE_PUBLIC_AND_PRIVATE = 0.2
VAT_RATE_RESIDENTIAL = 0.1
VAT_RATE_AGRICULTURAL_ACTIVITIES = 0.1
VAT_RATE_LIGHTING = 0.2



#Input validation func
def validation(x,text):
    number = int(input(f'{text}'))
    while number < x or type(x) != int:
        print('Invalid')
        number = input(f'{text}')
    return number

#Consumption calculator func

def consumption(previous,current):
    return current - previous

#Total fee calculator
def feeCalc(preferredTariff): #The function should have a parameter beacuse the function is going to be used in calculating profit or loss
    #Two Stage
    if consumerType == 'Public':
        if preferredTariff == 'Single':
            if limitExceed:
                totalFee = 30*SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW + limitExceedAmount*SINGLE_TIME_ENERGY_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH

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
        if preferredTariff == 'Single':
            if limitExceed:
                totalFee = 8*SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_LOW + limitExceedAmount*SINGLE_TIME_ENERGY_FEE_RESIDENTIAL_HIGH
                
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
        taxVAT = (taxECT + UNIT_DISTRIBUTION_FEE_INDUSTRIAL)*VAT_RATE_INDUSTRIAL
        
    elif consumerType == 'Public and Private':
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH
        taxECT = totalConsumptionFee*ECT_RATE_NOT_INDUSTRIAL
        taxVAT = (taxECT + UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_HIGH)
        
    elif consumerType == 'Residential':
        taxECT = totalConsumptionFee*ECT_RATE_NOT_INDUSTRIAL
        if martyrOrVeteran:
            unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_RESIDENTIAL_FAMILY_MARTYRS
            taxVAT = (taxECT + UNIT_DISTRIBUTION_FEE_RESIDENTIAL_FAMILY_MARTYRS)*VAT_RATE_RESIDENTIAL
            
        else:
            taxVAT = (taxECT+UNIT_DISTRIBUTION_FEE_RESIDENTIAL_HIGH)*VAT_RATE_RESIDENTIAL
            unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_PUBLIC_AND_PRIVATE_SECTOR_LOW
            
    elif consumerType == 'Agricultural':
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_AGRICULTURAL_ACTIVITIES
        taxECT = totalConsumptionFee*ECT_RATE_NOT_INDUSTRIAL
        taxVAT = (taxECT+UNIT_DISTRIBUTION_FEE_AGRICULTURAL_ACTIVITIES)*VAT_RATE_AGRICULTURAL_ACTIVITIES
        
    else: #Lightning
        unitDistribution = totalConsumption*UNIT_DISTRIBUTION_FEE_LIGHTING
        taxECT = totalConsumptionFee*ECT_RATE_NOT_INDUSTRIAL
        taxVAT = (taxECT + UNIT_DISTRIBUTION_FEE_LIGHTING)*VAT_RATE_LIGHTING
        
    
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
        preferredTariff = 'Multi'
    else:
        preferredTariff = 'Single'
    
    newTotalConsumptionFee = feeCalc(preferredTariff)
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

        profitLossAmount = -(difference)
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

    consumerNo = input('Please enter your consumer no, 0 to exit')
    martyrOrVeteran = False
    if consumerNo == 0:
        break
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


    if (not martyrOrVeteran) and (consumerType != 'L' or consumerType != 'l'):
        preferredTariff = input('Enter preferred tariff')
        while preferredTariff not in ['S','s','M','m']:
            print()
            preferredTariff = input()
        if preferredTariff == 'S' or preferredTariff == 's':
            preferredTariff = 'Single'
        else:
            preferredTariff = 'Multi'
        



    previousDaytime = validation(0,'Please enter previous daytime')
    currentDaytime = validation(previousDaytime,'Please enter current daytime')
    previousPeak = validation(0,'Enter previous peak')
    currentPeak = validation(previousPeak,'Please enter current peak')
    previousNight = validation(0,'Please enter previous night')
    currentNight = validation(previousPeak,'Please enter current night')


    daysBetween = validation(1,'Please enter days between')
    totalConsumptionOfYear = validation(0,'Please enter total consumption made in the year')
    totalConsumption = consumption(previousDaytime,currentDaytime) + consumption(previousPeak,currentPeak) + consumption(previousNight,currentNight)

    dailyAverage = totalConsumption/daysBetween

    if consumerType == 'Public and Private':
        if dailyAverage <= 30: 
            limitExceed = False
        else:
            limitExceed = True
            limitExceedAmount = (30-dailyAverage)*daysBetween
        if preferredTariff == 'Single':
            publicSingle += 1
    elif consumerType == 'Residential':
        if totalConsumption / daysBetween <= 8:
            limitExceed = False
        else:
            limitExceed = True
            limitExceedAmount = (30-dailyAverage)*daysBetween





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
            consumptionCounterIndustrial += 1
        case 'Residential':
            counterResidential+=1
            consumptionCounterResidential +=1
        case 'Public and Private':
            counterPublic+=1
            consumptionCounterPublic += 1
        case 'Agricultural':
            counterAgricultural+=1
            consumptionCounterAgricultural+=1
        case 'Lightning':
            counterLightning+=1
            consumptionCounterLightning+=1

           
        


    #Total statistics of all consumers by using counters
    
    allCustomersConsumption += totalConsumption
    if consumerType == 'Public and Private':
        publicDailyAverageCounter += dailyAverage
    
    allCustomersGDZRevenue += totalConsumptionFee + taxCalc('VAT',totalConsumptionFee)
    allCustomersECTRevenue += totalECT
    allCustomersVATRevenue  += totalVAT






        
    #Prints for each consumer

    print(consumerNo)
    print(consumerType)
    print(consumption(previousDaytime,currentDaytime))
    print(consumption(previousPeak,currentPeak))
    print(consumption(previousNight,currentNight))
    print(totalConsumption)
    print(round(totalConsumptionFee,2))
    print(round(totalECT,2))
    print(round(totalVAT,2))
    print(round(totalInvoice,2))

    
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
print(f'Percentage: {counterIndustrial/totalConsumers*100}')
print(f'Average electricty consumption: {consumptionCounterIndustrial/counterIndustrial}')
print(f'Total electricty consumption for Industrial {consumptionCounterIndustrial}')

print('For consumer type Public, Private and Other:')
print(f'Number of consumers: {counterPublic} ')
print(f'Percentage: {counterPublic/totalConsumers*100}')
print(f'Average electricty consumption: {consumptionCounterPublic/counterPublic}')
print(f'Total electricty consumption for Industrial {consumptionCounterPublic}')

print('For consumer type Residential:')
print(f'Number of consumers: {counterResidential} ')
print(f'Percentage: {counterResidential/totalConsumers*100}')
print(f'Average electricty consumption: {consumptionCounterResidential/counterResidential}')
print(f'Total electricty consumption for Industrial {consumptionCounterResidential}')

print('For consumer type Agricultural Activites:')
print(f'Number of consumers: {counterAgricultural} ')
print(f'Percentage: {counterAgricultural/totalConsumers*100}')
print(f'Average electricty consumption: {consumptionCounterAgricultural/counterAgricultural}')
print(f'Total electricty consumption for Industrial {consumptionCounterAgricultural}')

print('For consumer type Lightning:')
print(f'Number of consumers: {counterLightning} ')
print(f'Percentage: {counterLightning/totalConsumers*100}')
print(f'Average electricty consumption: {consumptionCounterLightning/counterLightning}')
print(f'Total electricty consumption for Industrial {consumptionCounterLightning}')

print(f'Bornova\s total consumption is {allCustomersConsumption}')

print(f'Number of public, private and other who prefer single{publicSingle}')
print(f'Number of public, private and other who prefer multi{publicMulti}')
print(f'Number of public, private and other single percentage{publicSingle/counterPublic}')

print(f'Number of Industry consumer who is over 10000kWh or 100000TL and their percentage: {overusageIndustry}, {overusageIndustry/counterIndustrial}')
print(f'Consumer no of the residential type with the highest daily average consumption: {maxResidentialDailyAverageNo}')
print(f'This consumers daily average electricity usage: {maxResidentialDailyAverage}')
print(f'This consumers total bill: {maxTotalInvoiceDailyAverage}')

print(f'Consumer no of highest total bill other than residential: {maxTotalInvoiceNo}')
print(f'Consumer type of this consumer: {maxTotalInvoiceType}')
print(f'Daily average electricity consumption of this consumer: {maxTotalInvoiceDailyAverage}')
print(f'Total bill amount of this consumer: {maxTotalInvoice}')

print(f'Total revenue earned by GDZ{allCustomersGDZRevenue}')
print(f'Total revenue of municipality {allCustomersECTRevenue}')
print(f'Total revenue of the state {allCustomersVATRevenue}')

print(f'The precentage of those who made a loss {counterMultiLossConsumers/counterOtherThanMartyrLightning*100}')

























        

                
            




































            