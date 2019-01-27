package com.example.cargothefttracker;

import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class TruckListRecyclerViewAdapter extends RecyclerView.Adapter<TruckViewHolder> {

    private TruckItemListener mListener;
    private List<TruckModel> truckModels;

    public TruckListRecyclerViewAdapter(){
        this.truckModels = new ArrayList<>();
    }


    @NonNull
    @Override
    public TruckViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View truckView = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.truck_item_view, viewGroup, false);
        TruckViewHolder truckViewHolder = new TruckViewHolder(truckView);

        return truckViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull TruckViewHolder truckViewHolder, int i) {
        TruckModel truck = truckModels.get(i);
        truckViewHolder.setup(truck);
        truckViewHolder.setListener(mListener);
    }

    @Override
    public int getItemCount() {
        return truckModels.size();
    }

    public void setTruckList(List<TruckModel> truckList) {
        this.truckModels = truckList;
    }

    public void setListener(TruckItemListener listener){
        this.mListener = listener;
    }
}

class TruckViewHolder extends RecyclerView.ViewHolder {

    private TextView truckIdTextView;   //added this
    private TruckItemListener mItemListener;
    private TruckModel truckModel;


    public TruckViewHolder(@NonNull View itemView) {
        super(itemView);
        this.truckIdTextView = itemView.findViewById(R.id.truck_id);  //added this


        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (mItemListener == null)  return;

                mItemListener.itemPressed(truckModel);

            }
        });
    }

    public void setup(TruckModel truck) {
        this.truckModel = truck;
        this.truckIdTextView.setText(truck.getDeviceID());
        if (truck.getLikelihood().equals("High"))  {
            this.truckIdTextView.setTextColor(0xFF800000);
        }
        else if (truck.getLikelihood().equals("Medium")) {
            this.truckIdTextView.setTextColor(0xFFFFCC00);
        }
        else {
            this.truckIdTextView.setTextColor(0xFF009933);
        }
    }

    public void setListener(TruckItemListener truckListener){
        this.mItemListener = truckListener;

    }


}
