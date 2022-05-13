export class SteppersController {
  public activeStep: number = 1;

  public steps: number = 3;

  public step: number = 1;

  public nextStep() {
    this.activeStep += 1;
    if (this.activeStep === this.steps + 1) {
      this.activeStep = this.step;
    }
  }
}
