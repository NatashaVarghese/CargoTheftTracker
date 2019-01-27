package com.example.cargothefttracker;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.util.ArrayList;
import java.util.List;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();

    private RecyclerView mTructList;
    private TruckListRecyclerViewAdapter mTruckListAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.mTructList = findViewById(R.id.truck_list_view);

        this.mTruckListAdapter = new TruckListRecyclerViewAdapter();

        this.mTruckListAdapter.setListener(new TruckItemListener() {
            @Override
            public void itemPressed(TruckModel pressed) {
                Intent truckActivityIntent = new Intent(MainActivity.this, TruckActivity.class);
                truckActivityIntent.putExtra("truck", pressed);
                startActivity(truckActivityIntent);
            }
        });

        this.mTructList.setHasFixedSize(true);
        this.mTructList.setLayoutManager(new LinearLayoutManager(this));
        this.mTructList.setAdapter(this.mTruckListAdapter);

        FetchTruckNames fetchTruckNames = new FetchTruckNames(new NetworkDataListener() {

            @Override
            public void dataFetched(JsonObject json) {
                JsonArray numList = json.get("data").getAsJsonArray();
                Gson gson = new Gson();
                List<TruckModel> truckList = new ArrayList<>();
                for (int i = 0; i < numList.size(); i++) {
//                    Log.d(TAG, "Data at " + i + ": " + numList.get(i));
//                    JsonObject truckObject = numList.get(i).getAsJsonObject();
                    truckList.add(gson.fromJson(numList.get(i), TruckModel.class));
                }

                mTruckListAdapter.setTruckList(truckList);
                mTruckListAdapter.notifyDataSetChanged();

//                this.data = numList;
            }

            @Override
            public void failed(int status, String error) {
                Log.d(TAG, "Failed to fetch truck data");
            }

        });
        fetchTruckNames.execute();
        //This gave me an error :(

        //setTruckList needs the
//        this.mTruckListAdapter.setTruckList();
//        this.mTruckListAdapter.notifyDataSetChanged();



    }
}

class FetchTruckNames extends AsyncTask<Void, Void, JsonObject> {

    NetworkDataListener dataListener;

    public FetchTruckNames(NetworkDataListener listener) {
        this.dataListener = listener;
    }

    @Override
    protected JsonObject doInBackground(Void... voids) {

        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url("http://10.0.2.2:5000/trucks")
                .get()
                .addHeader("cache-control", "no-cache")
                .addHeader("Postman-Token", "eab1eaa4-a6ab-4889-a1d0-218af5337c19")
                .build();

        try {
            Response response = client.newCall(request).execute();
            String responseData = response.body().string();

            Gson gson = new Gson();
            JsonObject jsonObject = gson.fromJson(responseData, JsonObject.class);

            return jsonObject;
        }
        catch (Exception e){e.printStackTrace();}
        return null;
    }


    @Override
    protected void onPostExecute(JsonObject jsonElements) {
        super.onPostExecute(jsonElements);

        dataListener.dataFetched(jsonElements);
    }

    public void setTruckListener(NetworkDataListener listener) {
        this.dataListener = listener;
    }

}
