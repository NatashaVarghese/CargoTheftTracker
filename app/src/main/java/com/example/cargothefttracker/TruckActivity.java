package com.example.cargothefttracker;

import android.os.AsyncTask;
import android.support.v4.app.FragmentActivity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import org.json.JSONObject;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class TruckActivity extends FragmentActivity implements OnMapReadyCallback {

    private static final String TAG = TruckActivity.class.getSimpleName();

    private GoogleMap map;

    private TruckModel truck;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_truck);

        this.truck = getIntent().getParcelableExtra("truck");

        MapFragment mapFragment = (MapFragment) getFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        FetchTruckData fetchTruckData = new FetchTruckData(new NetworkDataListener() {
            @Override
            public void dataFetched(JsonObject json) {
                JsonArray numList = json.get("data").getAsJsonArray();
                for (int i = 0; i < numList.size(); i++) {
                    Log.d(TAG, "Latitude is: " + numList.get(i).getAsJsonObject().get("lat").getAsFloat());
                    JsonObject truckObject = numList.get(i).getAsJsonObject();
                    float latitude = truckObject.get("lat").getAsFloat();
                    float longitude = truckObject.get("long").getAsFloat();

                    if (map == null) {
                        continue;
                    }

                    String time = truckObject.get("date").getAsString();

                    MarkerOptions markerOptions = new MarkerOptions();
                    markerOptions.position(new LatLng(latitude, longitude));
                    markerOptions.snippet("Threat Level: " + truck.getLikelihood() + ", Timestamp: " + time);
                    markerOptions.title("VIN: " + truck.getDeviceID());

                    map.addMarker(markerOptions);
                    map.moveCamera(CameraUpdateFactory.newLatLng(new LatLng(latitude, longitude)));
                    map.moveCamera(CameraUpdateFactory.zoomTo(9));
                }
                Log.d(TAG, "Successfully fetched truck data: " + json);
            }

            @Override
            public void failed(int status, String error) {
                Log.d(TAG, "FAiled to fetch truck data");
            }
        });

        fetchTruckData.execute(this.truck.getDeviceID());

    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        Log.d(TAG, "Map is ready");
        this.map = googleMap;
    }
}

class FetchTruckData extends AsyncTask<String, Void, JsonObject> {

    NetworkDataListener dataListener;

    public FetchTruckData(NetworkDataListener listener){
        this.dataListener = listener;
    }


    @Override
    protected JsonObject doInBackground(String... truckList) {
        if (truckList.length == 0) return null;

        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url("http://10.0.2.2:5000/truckEvents/" + truckList[0])
                .get()
                .addHeader("cache-control", "no-cache")
                .addHeader("Postman-Token", "55c7f439-e8fb-49c2-9dfd-437675f4b2c2")
                .build();


        try {
            Response response = client.newCall(request).execute();
            String responseData = response.body().string();

            Gson gson = new Gson();
            JsonObject jsonObject = gson.fromJson(responseData, JsonObject.class);

            return jsonObject;
        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }

    @Override
    protected void onPostExecute(JsonObject jsonElements) {
        super.onPostExecute(jsonElements);
        dataListener.dataFetched(jsonElements);
    }
}
