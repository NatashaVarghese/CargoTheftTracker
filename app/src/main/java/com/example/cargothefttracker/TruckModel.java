package com.example.cargothefttracker;

import android.os.Parcel;
import android.os.Parcelable;

import com.google.gson.annotations.SerializedName;

public class TruckModel implements Parcelable {
    @SerializedName("vin")
    private String deviceID;

    @SerializedName("threatLevel")
    private int likelihood;


    public TruckModel(String device_serial, int likelihood){
        this.deviceID = device_serial;
        this.likelihood = likelihood;
    }

    protected TruckModel(Parcel in) {
        deviceID = in.readString();
        likelihood = in.readInt();
    }

    public static final Creator<TruckModel> CREATOR = new Creator<TruckModel>() {
        @Override
        public TruckModel createFromParcel(Parcel in) {
            return new TruckModel(in);
        }

        @Override
        public TruckModel[] newArray(int size) {
            return new TruckModel[size];
        }
    };

    public String getDeviceID() {
        return deviceID;
    }

    public void setDeviceID(String deviceID) {
        this.deviceID = deviceID;
    }

    public String getLikelihood() {
        if (likelihood == 2) return "High";
        if (likelihood == 1) return "Medium";
        return "Low";
    }

    public void setLikelihood(int likelihood) {
        this.likelihood = likelihood;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {

        dest.writeString(deviceID);
        dest.writeInt(likelihood);
    }
}
