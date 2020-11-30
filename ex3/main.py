# # #
# # # some heroes race statistics .  fde-capu . 2012
# # # written for Python 3.7.3
# # #

import numpy as np
import pandas as pd

# # #

df = pd.read_csv('herois-corrida.txt', sep = ';')
TIM, SUP, VOL, LAP, VEL = df.columns
HID = "Código do herói"
NAM = "Nome do herói"
POS = "posição"
CVL = "voltas completadas"
MED = "média de velocidade total"

def	posicao_de_chegada(df):
	cut = df[df[VOL] == df[VOL].max()][[NAM, TIM]].copy()
	cut = cut.sort_values(by = [TIM])
	cut.reset_index(inplace = True, drop = True)
	cut.reset_index(inplace = True)
	cut = cut.rename(columns = {"index": POS})
	cut[POS] = cut[POS].apply(lambda _: _ + 1)
	cut.drop([TIM], axis = 1, inplace = True)
	cut = cut.set_index([POS])
	return cut

def	codigos_dos_herois(df):
	cut = df[[NAM, HID]].copy()
	cut = cut.groupby(NAM).first()
	cut = cut.sort_values(by = [HID])
	cut.reset_index(inplace = True)
	cut = cut.reindex(columns = [HID, NAM])
	cut = cut.set_index([HID])
	return cut

def	nomes_dos_herois(df):
	cut = pd.DataFrame(pd.unique(df[NAM]), columns = [NAM])
	cut = cut.sort_values(by = [NAM])
	cut.reset_index(inplace = True, drop = True)
	return cut

def	get_race_end(df):
	return df[df[VOL] == df[VOL].max()][TIM].min()

def	quantidade_de_voltas_completadas(df):
	cut = df[[TIM, NAM, VOL]].copy()
	finish_line = get_race_end(df)
	cut = cut[cut[TIM] <= finish_line]
	cut = cut.sort_values(TIM).groupby(NAM).last()
	cut.drop([TIM], axis = 1, inplace = True)
	cut = cut.rename(columns = {VOL: CVL})
	return cut

def	tempo_total_de_prova(df):
	race_start = df[TIM].min() - df[df[VOL] == 1][LAP].min()
	finish_line = get_race_end(df)
	tmp = pd.to_timedelta(finish_line - race_start)
	return tmp

def melhor_volta_por_heroi(df):
	cut = df[[NAM, LAP, VOL]].copy()
	cut = cut.sort_values(LAP).groupby(NAM).first()
	cut = cut.sort_values(LAP)
	return cut

def	velocidade_media_por_heroi(df):
	cut = df[[NAM, VEL]].copy()
	cut = cut.groupby([NAM]).agg({VEL: [np.mean]})
	cut[MED] = cut[VEL]
	cut.drop([VEL], axis = 1, inplace = True)
	cut = cut.sort_values(by = [MED], ascending = False)
	return cut

# # #

df[TIM] = pd.to_datetime(df[TIM])
df[SUP] = df[SUP].apply(lambda _: str(_))
df[LAP] = df[LAP].apply(lambda _: "00:0" + str(_))
df[LAP] = pd.to_timedelta(df[LAP])
df[VOL] = df[VOL].apply(lambda _: int(_))
df[VEL] = df[VEL].apply(lambda _: float(_.replace(',', '.')))
df[HID] = df[SUP].apply(lambda _: str(_).split('–')[0])
df[NAM] = df[SUP].apply(lambda _: str(_).split('–')[1])
df.drop([SUP], axis = 1, inplace = True)

print (df)
print (df.info())
print ("\n---------\n")
print ("\nPosição de chegada:")
print (posicao_de_chegada(df))
#print ("\n---------\n")
print ("\nCódigos dos Super-Heróis:")
print (codigos_dos_herois(df))
#print ("\n---------\n")
print ("\nNomes dos Heróis:")
print (nomes_dos_herois(df))
#print ("\n---------\n")
print ("\nQuantidade de voltas completadas ao término (1 colocado = 4 voltas):")
print (quantidade_de_voltas_completadas(df))
#print ("\n---------\n")
print ("\nTempo total de prova ao término (1º colocado = 4 voltas):")
print (tempo_total_de_prova(df))
#print ("\n---------\n")
print ("\nMelhor volta de cada super herói:")
print (melhor_volta_por_heroi(df))
#print ("\n---------\n")
print ("\nMelhor volta da corrida:")
print (melhor_volta_por_heroi(df).head(1))
#print ("\n---------\n")
print ("\nVelocidade média de cada herói:")
print (velocidade_media_por_heroi(df))
#print ("\n---------\n")
