//Sandra Saba
package Main;

import java.awt.Color;
import java.util.LinkedList;
import java.util.Queue;
import Data.Vector2D;
import logic.Control;
import timer.stopWatchX;

public class Main{
	// Fields (Static) below...
	public static Color s = new Color(50,100,200); 
	public static boolean isImageDrawn = false;
	public static stopWatchX timer = new stopWatchX(300);
	public static Queue <Vector2D> vecs1 = new LinkedList<>();
	public static Queue <Vector2D> vecs2 = new LinkedList<>();
	public static Vector2D currentVec = new Vector2D(-100,-100);
	// End Static fields...
	
	public static void main(String[] args) {
		Control ctrl = new Control();				// Do NOT remove!
		ctrl.gameLoop();							// Do NOT remove!
	}
	
	/* This is your access to things BEFORE the game loop starts */
	public static void start(){
		// TODO: Code your starting conditions here...NOT DRAW CALLS HERE! (no addSprite or drawString)
			Vector2D temp = new Vector2D(0,0);
			vecs1.add(temp);
			for (int i =0; i<6 ;i++) {
				//currentVec = vecs1.remove();
				temp.adjustX(175);
				vecs1.add(temp);	
			}
			
		//	vecs2 = vecs1;
			//currentVec = vecs1.remove(); //nothing?!

//temp.setX(444); vecs1.add(temp); temp.setX(666); vecs1.add(temp); temp.setX(888); vecs1.add(temp);
//temp.setX(1070); vecs1.add(temp); temp.setX(0); vecs1.add(temp);
			
	}
	
	/* This is your access to the "game loop" (It is a "callback" method from the Control class (do NOT modify that class!))*/
	public static void update(Control ctrl) {
		// TODO: This is where you can code! (Starting code below is just to show you how it works)
		
		if(isImageDrawn) {
			start();
			
				ctrl.addSpriteToFrontBuffer(currentVec.getX(), currentVec.getY(), "pentagon");						 				// Add a tester sprite to render list by tag (Remove later! Test only!)
				
		}
		ctrl.drawString(0, 150, "Sandra Saba", s); // Test drawing text on screen where you want (Remove later! Test only!)
		
		//ctrl.addSpriteToFrontBuffer(currentVec.getX(), currentVec.getY(), "pentagon");
		
		while(timer.isTimeUp() || ! isImageDrawn) {
			
			currentVec = vecs1.remove();
			timer.resetWatch();
		}
		
	}
	
	// Additional Static methods below...(if needed)

}
