package org.parallel;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class BusinessLogicSimulation {

    public void startSimulation(int timeInMillis) {
        try {
            Thread.sleep(timeInMillis);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
