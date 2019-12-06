import keras
import numpy as np
import fasttext as ft
from sklearn.externals import joblib

#Nama barang autoEnco
inputs = keras.layers.Input(shape=(300,))
encoder = keras.layers.Dense(256,activation='relu')(inputs)
encoder = keras.layers.Dense(128,activation='relu')(encoder)
encoder = keras.layers.Dense(64,activation='relu')(encoder)
encoder = keras.layers.Dense(32,activation='relu')(encoder)
code = keras.layers.Dense(16,activation='relu')(encoder)
decoder = keras.layers.Dense(32,activation='relu')(code)
decoder = keras.layers.Dense(64,activation='relu')(decoder)
decoder = keras.layers.Dense(128,activation='relu')(decoder)
decoder = keras.layers.Dense(256,activation='relu')(decoder)
decoder = keras.layers.Dense(300,activation='relu')(decoder)
model_enco = keras.models.Model(inputs=inputs,outputs=decoder)
Adam = keras.optimizers.Adam(lr=0.005)
model_enco.compile(loss='mean_squared_error',optimizer=Adam)
model_enco.load_weights("./budget/bobot_nama.h5")
model_enco._make_predict_function()

#Harga barang autoEnco
inputs_2 = keras.layers.Input(shape=(5,))
encoder_2 = keras.layers.Dense(4,activation='relu')(inputs_2)
encoder_2 = keras.layers.Dense(3,activation='relu')(encoder_2)
code_2 = keras.layers.Dense(3,activation='relu')(encoder_2)
decoder_2 = keras.layers.Dense(3,activation='relu')(code_2)
decoder_2 = keras.layers.Dense(4,activation='relu')(decoder_2)
decoder_2 = keras.layers.Dense(5,activation='relu')(decoder_2)
model_enco_2 = keras.models.Model(inputs=inputs_2,outputs=decoder_2)
Adam_2 = keras.optimizers.Adam(lr=0.005)
model_enco_2.compile(loss='mean_squared_error',optimizer=Adam)
model_enco_2.load_weights('./budget/bobot_harga.h5')
model_enco_2._make_predict_function()

class Anomali():
    def __init__(self):
        self.autoenco_nama = model_enco
        self.autoenco_harga = model_enco_2
        self.st_harga = joblib.load("./budget/scaler_harga.pkl")
        self.st_satuan = joblib.load("./budget/scaler_satuan.pkl")
        #self.autoenco = self.bikin_model(alamat_weights)
        #self.embed = model
        #self.embed= ft.load_model('./budget/cc.id.300.bin')

    def cek_nama(self,nama,epsilon=0.3):
        nama = nama.lower()
        m1 = self.embed.get_sentence_vector(nama)
        m2 = self.autoenco_nama.predict(m1.reshape(1,-1))
        val = (self.findCosineSimiliarity(m1,np.squeeze(m2)))
        print(val)
        if val>epsilon:
            return("Normal Barang")
        else:
            return("Anomali Barang")

    def bikin_model(self,alamat):
        inputs = keras.layers.Input(shape=(300,))
        encoder = keras.layers.Dense(256,activation='relu')(inputs)
        encoder = keras.layers.Dense(128,activation='relu')(encoder)
        encoder = keras.layers.Dense(64,activation='relu')(encoder)
        encoder = keras.layers.Dense(32,activation='relu')(encoder)
        code = keras.layers.Dense(16,activation='relu')(encoder)
        decoder = keras.layers.Dense(32,activation='relu')(code)
        decoder = keras.layers.Dense(64,activation='relu')(decoder)
        decoder = keras.layers.Dense(128,activation='relu')(decoder)
        decoder = keras.layers.Dense(256,activation='relu')(decoder)
        decoder = keras.layers.Dense(300,activation='relu')(decoder)
        model_enco = keras.models.Model(inputs=inputs,outputs=decoder)
        optim = keras.optimizers.Adam(lr=0.001)
        model_enco.load_weights(alamat)
        model_enco.compile(loss='mean_squared_error',optimizer=optim)
        return model_enco

    def findCosineSimiliarity(self,a,b):
        cos = np.dot(a,b)
        norma = np.linalg.norm(a)
        normb = np.linalg.norm(b)
        return cos/(norma*normb)

    def cek_harga(self,satuan,harga,inventaris_siswa,inventaris_guru,inventaris_sekolah,epsilon=0.3):
        satuan = np.array([satuan])
        harga = np.array([harga])
        satuan = np.log(satuan)
        harga = np.log(harga)
        satuan = self.st_satuan.transform(satuan.reshape(1,-1))
        harga = self.st_harga.transform(harga.reshape(1,-1))
        #Satuan_log_st, harga_log_st,siswa,guru,sekolah
        d1 = np.array([np.squeeze(satuan), np.squeeze(harga), inventaris_siswa,inventaris_guru,inventaris_sekolah])
        d2 = self.autoenco_harga.predict(d1.reshape(1,-1))
        val = self.findCosineSimiliarity(d1,np.squeeze(d2))
        print(val)
        if val > epsilon:
            return "Normal harga"
        else:
            return "Anomali harga"
