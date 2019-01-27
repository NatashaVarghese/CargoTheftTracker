package com.example.cargothefttracker;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

public interface NetworkDataListener {

    public void dataFetched(JsonObject json);

    public void failed(int status, String error);

}
