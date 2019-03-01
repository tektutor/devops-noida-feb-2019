package org.tektutor;

import static org.junit.Assert.*;
import org.junit.Test;

public class AppTest {

    @Test
    public void testSayHello() {

        App app = new App();

        String actualResponse = app.sayHello();
        String expectedResponse = "Hello DevOps!";

        assertEquals ( expectedResponse, actualResponse );

    }

}

        
